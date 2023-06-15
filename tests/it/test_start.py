from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
from asreview import get_data_home
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
from asreview_simulation.cli import cli
from tests.it.helpers import compare_data_csv
from tests.it.helpers import compare_project_json
from tests.it.helpers import compare_results_sql
from tests.it.helpers import compare_settings_metadata_json
from tests.it.helpers import get_model_combinatorics
from tests.it.helpers import get_xfails
from tests.it.helpers import rename_simulation_results
from tests.it.helpers import unzip_simulate_results


def test_with_minimal_args():
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

    dataset = "benchmark:van_de_Schoot_2017"

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


@pytest.mark.parametrize("parameterization", get_model_combinatorics())
def test_with_model_combinations(parameterization):
    """
    - seeded random prior with 5 included and 5 excluded
    - generate 20 instances in each query
    - stop querying after 5 queries for a total of 110 records
    - use one dataset, benchmark:van_de_Schoot_2017
    - try different combinations of balancer, classifier, extractor, querier
    - use default parameterization for each model
    """

    def run_asreview_simulate_cli():
        embedding_pars = list()
        if fex == "embedding-idf" or fex == "embedding-lstm":
            embedding_pars += ["--embedding"]
            embedding_pars += [str(get_data_home() / "fasttext.cc.en.300.vec")]
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
            *embedding_pars,
            "--seed",
            "567",
            "--stop_if",
            "5",
            "--n_instances",
            "20",
            dataset,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        embedding_pars = list()
        if fex == "embedding-idf" or fex == "embedding-lstm":
            embedding_pars += ["--embedding"]
            embedding_pars += [str(get_data_home() / "fasttext.cc.en.300.vec")]
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
            *embedding_pars,
            f"qry:{qry}",
            "--n_instances",
            "20",
            "stp:n",
            "5",
            "start",
            "--dataset",
            dataset,
            "--seed",
            "567",
            str(p2),
        ]
        runner = CliRunner()
        result = runner.invoke(cli, args)
        assert result.exit_code == 0, "cli runner did not exit 0"
        rename_simulation_results(p2)

    dataset = "benchmark:van_de_Schoot_2017"
    bal, cls, fex, qry = parameterization.split(",")

    xfail, reason = get_xfails(parameterization)
    if xfail:
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