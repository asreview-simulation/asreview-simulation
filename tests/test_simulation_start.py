import hashlib
import json
import os
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
from asreview.datasets import DatasetManager
from asreview.entry_points import SimulateEntryPoint
from asreview.state.sqlstate import SQLiteState
from click.testing import CliRunner
from asreview_simulation import cli


def calc_hash(filename):
    with open(filename, "rb") as f:
        contents = f.read()
        return hashlib.sha256(contents).hexdigest()


def compare_data_csv(p1, p2, dataset):
    fname = (
        f"{dataset[10:]}.csv" if dataset.startswith("benchmark:") else f"{dataset}.csv"
    )
    assert calc_hash(p1 / "data" / fname) == calc_hash(p2 / "data" / fname)


def compare_project_json(p1, p2):
    with open(p1 / "project.json", "r") as f:
        expected = json.load(f)
    with open(p2 / "project.json", "r") as f:
        actual = json.load(f)

    assert actual["version"] == expected["version"]
    assert actual["mode"] == expected["mode"]
    assert actual["dataset_path"] == expected["dataset_path"]
    assert actual["feature_matrices"][0]["id"] == expected["feature_matrices"][0]["id"]
    assert (
        actual["feature_matrices"][0]["filename"]
        == expected["feature_matrices"][0]["filename"]
    )
    assert actual["reviews"][0]["status"] == expected["reviews"][0]["status"]


def compare_results_sql(
    p1, p2, test_metadata=False, test_prior_records=False, test_queried_records=False
):
    state1 = SQLiteState(read_only=True)
    state1._restore(p1, get_review_id(p1))
    df1 = state1.get_dataset()

    state2 = SQLiteState(read_only=True)
    state2._restore(p2, get_review_id(p2))
    df2 = state2.get_dataset()

    columns = [
        "record_id",
        "label",
        "classifier",
        "query_strategy",
        "balance_strategy",
        "feature_extraction",
        "training_set",
    ]

    if test_metadata is True:
        assert state1.version == state2.version
        assert state1.n_records == state2.n_records
        assert state1.n_priors == state2.n_priors
    if test_prior_records is True:
        results1 = df1.loc[df1.query_strategy == "prior", columns].values
        results2 = df2.loc[df2.query_strategy == "prior", columns].values
        assert bool((results1 == results2).all())
    if test_queried_records is True:
        assert bool((df1.values == df2.values).all())
    if (
        test_metadata is False
        and test_prior_records is False
        and test_queried_records is False
    ):
        raise "You probably wanted to test at least some aspects of the SQL file."


def compare_settings_metadata_json(p1, p2):
    settings1 = p1 / "reviews" / get_review_id(p1) / "settings_metadata.json"
    settings2 = p2 / "reviews" / get_review_id(p2) / "settings_metadata.json"
    assert calc_hash(settings1) == calc_hash(settings2)


def get_review_id(p):
    with open(p / "project.json", "r") as f:
        project_data = json.load(f)
    return project_data["reviews"][0]["id"]


def list_dataset_names():
    dataset_names = list()
    for group in DatasetManager().list():
        for dataset in group["datasets"]:
            dataset_names.append(f"{group['group_id']}:{dataset['dataset_id']}")
    return dataset_names


def rename_simulation_results(p):
    src = p.parent / Path(p.name + ".tmp")
    tgt = p
    os.rename(src, tgt)


@pytest.mark.parametrize("dataset", list_dataset_names())
def test_simulation_start_with_minimal_args(dataset):
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            dataset,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "start",
            "--dataset",
            dataset,
            str(p2),
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0
        rename_simulation_results(p2)

    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"
        run_asreview_simulate_cli()
        run_asreview_simulation_start_cli()

        # compare the two results
        compare_project_json(p1, p2)
        compare_data_csv(p1, p2, dataset)
        compare_settings_metadata_json(p1, p2)
        # sql tables are expected to be different due to random
        # seed differences, so no use in comparing that part
        compare_results_sql(p1, p2, test_metadata=True)


@pytest.mark.parametrize("dataset", list_dataset_names())
def test_simulation_start_with_seeded_random_prior(dataset):
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            "--init_seed",
            "42",
            dataset,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "sam:random",
            "--init_seed",
            "42",
            "start",
            "--dataset",
            dataset,
            str(p2),
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0
        rename_simulation_results(p2)

    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"
        run_asreview_simulate_cli()
        run_asreview_simulation_start_cli()

        # compare the two results
        compare_project_json(p1, p2)
        compare_data_csv(p1, p2, dataset)
        compare_settings_metadata_json(p1, p2)
        compare_results_sql(p1, p2, test_metadata=True, test_prior_records=True)


def unzip_simulate_results(p):
    src = p.parent / Path(p.name + ".tmp")
    tgt = p
    os.rename(tgt, src)
    with zipfile.ZipFile(src, "r") as f:
        f.extractall(tgt)
    os.remove(src)
