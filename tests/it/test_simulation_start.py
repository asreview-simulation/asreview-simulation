import itertools
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
import numpy
import pytest
from asreview.data import load_data
from asreview.entry_points import SimulateEntryPoint
from asreview.models.balance import list_balance_strategies
from asreview.models.classifiers import list_classifiers
from asreview.models.feature_extraction import list_feature_extraction
from asreview.models.query import list_query_strategies
from click.testing import CliRunner
from asreview_simulation.cli import cli
from tests.it.helpers import compare_data_csv
from tests.it.helpers import compare_project_json
from tests.it.helpers import compare_results_sql
from tests.it.helpers import compare_settings_metadata_json
from tests.it.helpers import list_dataset_names
from tests.it.helpers import rename_simulation_results
from tests.it.helpers import unzip_simulate_results


@pytest.mark.parametrize("dataset", list_dataset_names())
def test_simulation_start_seeded_with_random_prior_seeded(dataset):
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            "--init_seed",
            "42",
            "--n_prior_included",
            "5",
            "--n_prior_excluded",
            "5",
            "--seed",
            "567",
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
            "--n_included",
            "5",
            "--n_excluded",
            "5",
            "start",
            "--dataset",
            dataset,
            "--seed",
            "567",
            str(p2),
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0
        rename_simulation_results(p2)

    if sys.platform == "win32" and dataset.startswith("benchmark-nature:"):
        pytest.xfail(reason="data filename bug")

    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"

        # run
        run_asreview_simulate_cli()
        run_asreview_simulation_start_cli()

        # compare the two results
        compare_project_json(p1, p2)
        compare_data_csv(p1, p2, dataset)
        compare_settings_metadata_json(p1, p2)
        compare_results_sql(
            p1,
            p2,
            test_metadata=True,
            test_prior_records=True,
            test_queried_records=True,
        )


@pytest.mark.parametrize("dataset", list_dataset_names())
def test_simulation_start_unseeded_with_minimal_args(dataset):
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

    if sys.platform == "win32" and dataset.startswith("benchmark-nature:"):
        pytest.xfail(reason="data filename bug")

    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"

        # run
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
def test_simulation_start_unseeded_with_stopping_rule_and_handpicked_prior(dataset):
    def determine_valid_set_of_ids(n=5):
        as_data = load_data(dataset)
        return (
            numpy.where(as_data.labels == 0)[0].tolist()[:n]
            + numpy.where(as_data.labels == 1)[0].tolist()[:n]
        )

    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            "--stop_if",
            "0",
            "--prior_idx",
            *[str(elem) for elem in ids],
            "--",
            dataset,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "sam:handpicked",
            ",".join([str(elem) for elem in ids]),
            "stp:n",
            "0",
            "start",
            "--dataset",
            dataset,
            str(p2),
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0
        rename_simulation_results(p2)

    if sys.platform == "win32" and dataset.startswith("benchmark-nature:"):
        pytest.xfail(reason="data filename bug")

    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"
        ids = determine_valid_set_of_ids()

        # run
        run_asreview_simulate_cli()
        run_asreview_simulation_start_cli()

        # compare the two results
        compare_project_json(p1, p2)
        compare_data_csv(p1, p2, dataset)
        compare_settings_metadata_json(p1, p2)
        compare_results_sql(p1, p2, test_metadata=True, test_prior_records=True)


def get_model_combinatorics():
    bals = ["double"]  # [elem.name for elem in list_balance_strategies()]
    clss = [elem.name for elem in list_classifiers()]
    fexs = [elem.name for elem in list_feature_extraction()]
    qrys = ["max"]  # [elem.name for elem in list_query_strategies()]
    result = []
    for combination in itertools.product(*[bals, clss, fexs, qrys]):
        xfails = {
            "double,logistic,embedding-idf,max": ("xfail", "issue #34"),
            "double,lstm-base,embedding-idf,max": ("xfail", "issue #34"),
            "double,lstm-base,embedding-lstm,max": ("xfail", "tbd"),
            "double,lstm-base,doc2vec,max": ("xfail", "tbd"),
            "double,lstm-base,tfidf,max": ("xfail", "tbd"),
            "double,lstm-base,sbert,max": ("xfail", "tbd"),
            "double,lstm-pool,doc2vec,max": ("xfail", "tbd"),
            "double,lstm-pool,embedding-idf,max": ("xfail", "issue #34"),
            "double,lstm-pool,embedding-lstm,max": ("xfail", "tbd"),
            "double,lstm-pool,tfidf,max": ("xfail", "issue #21"),
            "double,lstm-pool,sbert,max": ("xfail", "tbd"),
            "double,nb,doc2vec,max": (
                "xfail",
                "ValueError: Negative values in data passed to MultinomialNB",
            ),
            "double,nb,embedding-idf,max": ("xfail", "issue #34"),
            "double,nb,sbert,max": (
                "xfail",
                "ValueError: Negative values in data passed to MultinomialNB",
            ),
            "double,nn-2-layer,doc2vec,max": ("xfail", "tbd"),
            "double,nn-2-layer,embedding-idf,max": ("xfail", "issue #34"),
            "double,nn-2-layer,embedding-lstm,max": ("xfail", "tbd"),
            "double,nn-2-layer,tfidf,max": ("xfail", "issue #33"),
            "double,nn-2-layer,sbert,max": ("xfail", "tbd"),
            "double,rf,embedding-idf,max": ("xfail", "issue #34"),
            "double,rf,embedding-lstm,max": ("xfail", "tbd"),
            "double,svm,embedding-idf,max": ("xfail", "issue #34"),
        }
        key = ",".join(combination)
        try:
            parameterization = (key,) + xfails[key]
        except KeyError:
            parameterization = (key,) + ("pass", "no_msg")
        result.append(parameterization)
    return result


@pytest.mark.parametrize(
    "combination, expected_status, reason", get_model_combinatorics()
)
def test_simulation_start_with_model_combination(combination, expected_status, reason):
    """
    - seeded random prior with 5 included and 5 excluded
    - stop querying after 90 records for a total of 100
    - use one dataset, benchmark:van_de_Schoot_2017
    - try different combinations of balancer, classifier, extractor, querier
    - use default parameterization for each model
    """

    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            "--init_seed",
            "42",
            "--n_prior_included",
            "5",
            "--n_prior_excluded",
            "5",
            "-m",
            cls,
            "-q",
            qry,
            "-b",
            bal,
            "-e",
            fex,
            "--seed",
            "567",
            "--stop_if",
            "90",
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
            "--n_included",
            "5",
            "--n_excluded",
            "5",
            f"bal:{bal}",
            f"cls:{cls}",
            f"fex:{fex}",
            f"qry:{qry}",
            "stp:n",
            "90",
            "start",
            "--dataset",
            dataset,
            "--seed",
            "567",
            str(p2),
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0
        rename_simulation_results(p2)

    dataset = "benchmark:van_de_Schoot_2017"
    bal, cls, fex, qry = combination.split(",")

    if sys.platform == "win32" and dataset.startswith("benchmark-nature:"):
        pytest.xfail(reason="data filename bug")

    if expected_status == "xfail":
        pytest.xfail(reason=reason)

    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"

        # run
        run_asreview_simulate_cli()
        run_asreview_simulation_start_cli()

        # compare the two results
        compare_project_json(p1, p2)
        compare_data_csv(p1, p2, dataset)
        compare_settings_metadata_json(p1, p2)
        compare_results_sql(
            p1,
            p2,
            test_metadata=True,
            test_prior_records=True,
            test_queried_records=True,
        )
