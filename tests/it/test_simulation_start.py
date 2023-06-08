import sys
import itertools
from pathlib import Path
from tempfile import TemporaryDirectory
import numpy
import pytest
from asreview.data import load_data
from asreview.entry_points import SimulateEntryPoint
from asreview.utils import list_model_names
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
    bals = list_model_names(entry_name="asreview.models.balance")
    clss = list_model_names(entry_name="asreview.models.classifiers")
    fexs = ["tfidf"] # list_model_names(entry_name="asreview.models.feature_extraction")
    qrys = list_model_names(entry_name="asreview.models.query")
    result = []
    for combination in itertools.product(*[bals, clss, fexs, qrys]):
        xfails = {
            "double,logistic,doc2vec,cluster": ("xfail", "tbd"),
            "double,logistic,embedding-idf,cluster": ("xfail", "tbd"),
            "double,logistic,embedding-idf,max_random": ("xfail", "tbd"),
            "double,logistic,embedding-idf,max_uncertainty": ("xfail", "tbd"),
            "double,logistic,embedding-idf,max": ("xfail", "tbd"),
            "double,logistic,embedding-idf,random": ("xfail", "tbd"),
            "double,logistic,embedding-idf,uncertainty": ("xfail", "tbd"),
            "double,logistic,embedding-lstm,cluster": ("xfail", "tbd"),
            "double,logistic,embedding-lstm,max_random": ("xfail", "tbd"),
            "double,logistic,embedding-lstm,max_uncertainty": ("xfail", "tbd"),
            "double,logistic,embedding-lstm,max": ("xfail", "tbd"),
            "double,logistic,embedding-lstm,random": ("xfail", "tbd"),
            "double,logistic,embedding-lstm,uncertainty": ("xfail", "tbd"),
            "double,logistic,sbert,cluster": ("xfail", "patience"),
            "double,logistic,sbert,max_random": ("xfail", "patience"),
            "double,logistic,sbert,max_uncertainty": ("xfail", "patience"),
            "double,logistic,sbert,max": ("xfail", "patience"),
            "double,logistic,sbert,random": ("xfail", "patience"),
            "double,logistic,sbert,uncertainty": ("xfail", "patience"),
            "double,lstm-base,tfidf,cluster": ("xfail", "issue #20"),
            "double,lstm-base,tfidf,max_random": ("xfail", "issue #20"),
            "double,lstm-base,tfidf,max_uncertainty": ("xfail", "issue #20"),
            "double,lstm-base,tfidf,max": ("xfail", "issue #20"),
            "double,lstm-base,tfidf,random": ("xfail", "issue #20"),
            "double,lstm-base,tfidf,uncertainty": ("xfail", "issue #20"),
            "double,lstm-pool,tfidf,cluster": ("xfail", "issue #21"),
            "double,lstm-pool,tfidf,max_random": ("xfail", "issue #21"),
            "double,lstm-pool,tfidf,max_uncertainty": ("xfail", "issue #21"),
            "double,lstm-pool,tfidf,max": ("xfail", "issue #21"),
            "double,lstm-pool,tfidf,random": ("xfail", "issue #21"),
            "double,lstm-pool,tfidf,uncertainty": ("xfail", "issue #21"),
            "double,nn-2-layer,tfidf,cluster": ("xfail", "tbd, results.sql not equal, maybe need to use almostequal"),
            "double,nn-2-layer,tfidf,max_random": ("xfail", "tbd, results.sql not equal, maybe need to use almostequal"),
            "double,nn-2-layer,tfidf,max_uncertainty": ("xfail", "tbd, results.sql not equal, maybe need to use almostequal"),
            "double,nn-2-layer,tfidf,max": ("xfail", "tbd, results.sql not equal, maybe need to use almostequal"),
            "double,nn-2-layer,tfidf,random": ("xfail", "tbd, results.sql not equal, maybe need to use almostequal"),
            "double,nn-2-layer,tfidf,uncertainty": ("xfail", "tbd, results.sql not equal, maybe need to use almostequal"),
            "double,svm,tfidf,cluster": ("xfail", "tbd"),
            "double,svm,tfidf,max_random": ("xfail", "tbd"),
            "double,svm,tfidf,max_uncertainty": ("xfail", "tbd"),
            "double,svm,tfidf,max": ("xfail", "tbd"),
            "double,svm,tfidf,random": ("xfail", "tbd"),
            "double,svm,tfidf,uncertainty": ("xfail", "tbd"),
            "simple,lstm-base,tfidf,cluster": ("xfail", "issue #20"),
            "simple,lstm-base,tfidf,max_random": ("xfail", "issue #20"),
            "simple,lstm-base,tfidf,max_uncertainty": ("xfail", "issue #20"),
            "simple,lstm-base,tfidf,max": ("xfail", "issue #20"),
            "simple,lstm-base,tfidf,random": ("xfail", "issue #20"),
            "simple,lstm-base,tfidf,uncertainty": ("xfail", "issue #20"),
            "simple,lstm-pool,tfidf,cluster": ("xfail", "issue #21"),
            "simple,lstm-pool,tfidf,max_random": ("xfail", "issue #21"),
            "simple,lstm-pool,tfidf,max_uncertainty": ("xfail", "issue #21"),
            "simple,lstm-pool,tfidf,max": ("xfail", "issue #21"),
            "simple,lstm-pool,tfidf,random": ("xfail", "issue #21"),
            "simple,lstm-pool,tfidf,uncertainty": ("xfail", "issue #21"),
            "simple,nn-2-layer,tfidf,cluster": ("xfail", "tbd"),
            "simple,nn-2-layer,tfidf,max_random": ("xfail", "tbd"),
            "simple,nn-2-layer,tfidf,max_uncertainty": ("xfail", "tbd"),
            "simple,nn-2-layer,tfidf,max": ("xfail", "tbd"),
            "simple,nn-2-layer,tfidf,random": ("xfail", "tbd"),
            "simple,nn-2-layer,tfidf,uncertainty": ("xfail", "tbd"),
            "simple,svm,tfidf,cluster": ("xfail", "tbd"),
            "simple,svm,tfidf,max_random": ("xfail", "tbd"),
            "simple,svm,tfidf,max_uncertainty": ("xfail", "tbd"),
            "simple,svm,tfidf,max": ("xfail", "tbd"),
            "simple,svm,tfidf,random": ("xfail", "tbd"),
            "simple,svm,tfidf,uncertainty": ("xfail", "tbd"),
            "triple,logistic,tfidf,max": ("xfail", "triple balancer is not implemented"),
            "triple,lstm-base,tfidf,max": ("xfail", "triple balancer is not implemented"),
            "triple,lstm-pool,tfidf,max": ("xfail", "triple balancer is not implemented"),
            "triple,nb,tfidf,max": ("xfail", "'triple balancer is not implemented'"),
            "triple,nn-2-layer,tfidf,max": ("xfail", "'triple balancer is not implemented'"),
            "undersample,lstm-base,tfidf,cluster": ("xfail", "issue #20"),
            "undersample,lstm-base,tfidf,max_random": ("xfail", "issue #20"),
            "undersample,lstm-base,tfidf,max_uncertainty": ("xfail", "issue #20"),
            "undersample,lstm-base,tfidf,max": ("xfail", "issue #20"),
            "undersample,lstm-base,tfidf,random": ("xfail", "issue #20"),
            "undersample,lstm-base,tfidf,uncertainty": ("xfail", "issue #20"),
            "undersample,lstm-pool,tfidf,cluster": ("xfail", "issue #21"),
            "undersample,lstm-pool,tfidf,max_random": ("xfail", "issue #21"),
            "undersample,lstm-pool,tfidf,max_uncertainty": ("xfail", "issue #21"),
            "undersample,lstm-pool,tfidf,max": ("xfail", "issue #21"),
            "undersample,lstm-pool,tfidf,random": ("xfail", "issue #21"),
            "undersample,lstm-pool,tfidf,uncertainty": ("xfail", "issue #21"),
            "undersample,nn-2-layer,tfidf,cluster": ("xfail", "tbd"),
            "undersample,nn-2-layer,tfidf,max_random": ("xfail", "tbd"),
            "undersample,nn-2-layer,tfidf,max_uncertainty": ("xfail", "tbd"),
            "undersample,nn-2-layer,tfidf,max": ("xfail", "tbd"),
            "undersample,nn-2-layer,tfidf,random": ("xfail", "tbd"),
            "undersample,nn-2-layer,tfidf,uncertainty": ("xfail", "tbd"),
            "undersample,svm,tfidf,cluster": ("xfail", "tbd"),
            "undersample,svm,tfidf,max_random": ("xfail", "tbd"),
            "undersample,svm,tfidf,max_uncertainty": ("xfail", "tbd"),
            "undersample,svm,tfidf,max": ("xfail", "tbd"),
            "undersample,svm,tfidf,random": ("xfail", "tbd"),
            "undersample,svm,tfidf,uncertainty": ("xfail", "tbd"),
        }
        key = ",".join(combination)
        try:
            parameterization = (key,) + xfails[key]
        except KeyError:
            parameterization = (key,) + ("pass", "no_msg")
        result.append(parameterization)
    return result


@pytest.mark.parametrize("combination, expected_status, reason", get_model_combinatorics())
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
