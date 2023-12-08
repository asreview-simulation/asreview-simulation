from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
from asreview import get_data_home
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
from asreviewcontrib.simulation._private.cli.cli import cli
from tests.helpers.compare_data_csv import compare_data_csv
from tests.helpers.compare_project_json import compare_project_json
from tests.helpers.compare_results_sql import compare_results_sql
from tests.helpers.compare_settings_metadata_json import compare_settings_metadata_json
from tests.helpers.get_model_combinatorics import get_model_combinatorics
from tests.helpers.get_xfails import get_xfails
from tests.helpers.unzip_simulate_results import unzip_simulate_results


def get_data_fnames():
    basepath = Path(__file__).parent.parent / "data"
    fnames = [
        "van_de_Schoot_2017.csv",
        "van_de_Schoot_2017.ris",
        "van_de_Schoot_2017.tsv",
        "van_de_Schoot_2017.xlsx",
    ]
    return [str(basepath / fname) for fname in fnames]


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.clr_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
@pytest.mark.ofn_none
def test_with_minimal_args_on_benchmark():
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            benchmark,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "start",
            "--benchmark",
            benchmark,
            "--out",
            str(p2),
            "--no-zip",
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0

    benchmark = "benchmark:van_de_Schoot_2017"

    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"

        # run
        run_asreview_simulate_cli()
        run_asreview_simulation_start_cli()

        # compare the two results
        compare_project_json(p1, p2)
        compare_data_csv(p1, p2, benchmark=benchmark)
        compare_settings_metadata_json(p1, p2)
        # sql tables are expected to be different due to random
        # seed differences, so no use in comparing that part
        compare_results_sql(p1, p2, test_metadata=True)


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.clr_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
@pytest.mark.ofn_none
@pytest.mark.parametrize("fname", get_data_fnames())
def test_with_minimal_args_on_user_supplied_data(fname):
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            fname,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "start",
            "--in",
            fname,
            "--out",
            str(p2),
            "--no-zip",
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0

    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"

        # run
        run_asreview_simulate_cli()
        run_asreview_simulation_start_cli()

        # compare the two results
        compare_project_json(p1, p2)
        compare_data_csv(p1, p2, input_file=fname)
        compare_settings_metadata_json(p1, p2)
        # sql tables are expected to be different due to random
        # seed differences, so no use in comparing that part
        compare_results_sql(p1, p2, test_metadata=True)


@pytest.mark.sam_random
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_nq
@pytest.mark.ofn_none
@pytest.mark.parametrize("parameterization", get_model_combinatorics())
def test_with_model_combinations(parameterization):
    """
    - seeded random prior with 5 included and 5 excluded
    - generate 20 instances in each query
    - stop querying after 5 queries for a total of 110 records
    - use one dataset, benchmark:van_de_Schoot_2017
    - try different combinations of classifier and extractor
    - balancer constant, set to 'double'
    - querier constant, set to 'max'
    - use default parameterization for each model
    """

    def run_asreview_simulate_cli():
        if fex in ["embedding-idf", "embedding-lstm"]:
            embedding_pars = [
                "--embedding",
                str(get_data_home() / "fasttext.cc.en.300.vec"),
            ]
        else:
            embedding_pars = list()
        args = [
            *embedding_pars,
            "--n_prior_included",
            "5",
            "--n_prior_excluded",
            "5",
            "--state_file",
            str(p1),
            "-m",
            clr,
            "-q",
            "max",
            "-b",
            "double",
            "-e",
            fex,
            "--init_seed",
            "42",
            "--seed",
            "567",
            "--n_instances",
            "20",
            "--stop_if",
            "5",
            benchmark,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        if fex in ["embedding-idf", "embedding-lstm"]:
            embedding_pars = [
                "--embedding",
                str(get_data_home() / "fasttext.cc.en.300.vec"),
            ]
        else:
            embedding_pars = list()
        args = [
            "sam-random",
            "--init_seed",
            "42",
            "--n_included",
            "5",
            "--n_excluded",
            "5",
            "bal-double",
            f"clr-{clr}",
            f"fex-{fex}",
            *embedding_pars,
            "qry-max",
            "--n_instances",
            "20",
            "stp-nq",
            "--n_queries",
            "5",
            "start",
            "--benchmark",
            benchmark,
            "--seed",
            "567",
            "--out",
            str(p2),
            "--no-zip",
        ]
        runner = CliRunner()
        result = runner.invoke(cli, args)
        assert result.exit_code == 0, "cli runner did not exit 0"

    benchmark = "benchmark:van_de_Schoot_2017"
    fex, clr = parameterization.split(",")

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

        # compare project.json from either result
        compare_project_json(p1, p2)

        # compare data/<filename>.csv from either result
        compare_data_csv(p1, p2, benchmark=benchmark)

        # compare reviews/<review_id>/settings_metadata.json from either result
        compare_settings_metadata_json(p1, p2)

        # for some classifier methods, records are not expected to
        # match due to nondeterministic methods
        nondeterministic_classifiers = [
            "lstm-base",
            "lstm-pool",
            "nn-2-layer",
            "rf",
            "svm",
        ]

        # compare reviews/<review_id>/results.sql from either result
        compare_results_sql(
            p1,
            p2,
            test_metadata=True,
            test_prior_records=True,
            test_queried_records=clr not in nondeterministic_classifiers,
        )
