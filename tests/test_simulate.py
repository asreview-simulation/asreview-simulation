import os
import hashlib
import zipfile
import json
import pytest
from tempfile import TemporaryDirectory
from pathlib import Path
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
from asreview_simulation import cli
from asreview.datasets import DatasetManager


def list_dataset_names():
    dataset_names = list()
    for group in DatasetManager().list():
        for dataset in group["datasets"]:
            dataset_names.append(f"{group['group_id']}:{dataset['dataset_id']}")
    return [n for n in dataset_names if n.startswith("benchmark:")]


@pytest.mark.parametrize("dataset", list_dataset_names())
def test_simulate_start(dataset):
    def calc_hash(filename):
        with open(filename, "rb") as f:
            contents = f.read()
            return hashlib.sha256(contents).hexdigest()

    def compare_data():
        fname = f"{dataset.split(':')[1]}.csv"
        assert calc_hash(p1 / "data" / fname) == calc_hash(p2 / "data" / fname)

    def compare_project_json():
        with open(p1 / "project.json", "r") as f:
            expected = json.load(f)
        with open(p2 / "project.json", "r") as f:
            actual = json.load(f)

        assert actual["version"] == expected["version"]
        assert actual["mode"] == expected["mode"]
        assert actual["dataset_path"] == expected["dataset_path"]
        assert actual["feature_matrices"][0]["id"] == expected["feature_matrices"][0]["id"]
        assert actual["feature_matrices"][0]["filename"] == expected["feature_matrices"][0]["filename"]
        assert actual["reviews"][0]["status"] == expected["reviews"][0]["status"]

    def compare_settings_metadata_json():
        settings1 = p1 / "reviews" / get_review_id(p1) / "settings_metadata.json"
        settings2 = p2 / "reviews" / get_review_id(p2) / "settings_metadata.json"
        assert calc_hash(settings1) == calc_hash(settings2)

    def get_review_id(p):
        with open(p / "project.json", "r") as f:
            project_data = json.load(f)
        return project_data["reviews"][0]["id"]

    def run_asreview_simulate_cli():
        args = [
            dataset,
            "--state_file", str(p1)
        ]
        SimulateEntryPoint().execute(args)
        # unzip simulate results
        src = p1.parent / Path(p1.name + ".tmp")
        tgt = p1
        os.rename(tgt, src)
        with zipfile.ZipFile(src, "r") as f:
            f.extractall(tgt)
        os.remove(src)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "start",
            "--dataset", dataset,
            str(p2)
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0
        # rename simulation results
        src = p2.parent / Path(p2.name + ".tmp")
        tgt = p2
        os.rename(src, tgt)

    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"
        run_asreview_simulate_cli()
        run_asreview_simulation_start_cli()

        # compare the two results
        compare_project_json()
        compare_data()
        compare_settings_metadata_json()

        print()
