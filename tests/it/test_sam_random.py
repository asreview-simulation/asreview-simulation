from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
from asreview_simulation.cli import cli
from tests.helpers import compare_data_csv
from tests.helpers import compare_project_json
from tests.helpers import compare_results_sql
from tests.helpers import compare_settings_metadata_json
from tests.helpers import unzip_simulate_results


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_nq
def test_with_init_seed():
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
            "--stop_if",
            "0",
            benchmark,
        ]
        SimulateEntryPoint().execute(args)
        unzip_simulate_results(p1)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "sam-random",
            "--init_seed",
            "42",
            "--n_included",
            "5",
            "--n_excluded",
            "5",
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
        compare_results_sql(
            p1,
            p2,
            test_metadata=True,
            test_prior_records=True,
            test_queried_records=True,
        )
