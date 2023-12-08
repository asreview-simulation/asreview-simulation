from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
from asreviewcontrib.simulation._private.cli.cli import cli
from tests.helpers.compare_data_csv import compare_data_csv
from tests.helpers.compare_project_json import compare_project_json
from tests.helpers.compare_results_sql import compare_results_sql
from tests.helpers.compare_settings_metadata_json import compare_settings_metadata_json
from tests.helpers.unzip_simulate_results import unzip_simulate_results


@pytest.mark.sam_handpicked
@pytest.mark.fex_tfidf
@pytest.mark.clr_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_nq
@pytest.mark.ofn_none
def test_with_records():
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            "--stop_if",
            "0",
            "--prior_record_id",
            *["0", "1", "2", "3", "4", "284", "335", "592", "675", "719"],
            "--",
            benchmark,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "sam-handpicked",
            "--records",
            "0,1,2,3,4,284,335,592,675,719",
            "stp-nq",
            "--n_queries",
            "0",
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
        compare_results_sql(p1, p2, test_metadata=True, test_prior_records=True)


@pytest.mark.sam_handpicked
@pytest.mark.fex_tfidf
@pytest.mark.clr_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_nq
@pytest.mark.ofn_none
def test_with_rows():
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            "--stop_if",
            "0",
            "--prior_idx",
            *["0", "1", "2", "3", "4", "284", "335", "592", "675", "719"],
            "--",
            benchmark,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "sam-handpicked",
            "--rows",
            "0,1,2,3,4,284,335,592,675,719",
            "stp-nq",
            "--n_queries",
            "0",
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
        compare_results_sql(p1, p2, test_metadata=True, test_prior_records=True)
