from pathlib import Path
from tempfile import TemporaryDirectory
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
from asreview_simulation.cli import cli
import asreview
import asreview_simulation
import unittest.mock


class BailError(Exception):
    pass


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
            dataset,
        ]
        SimulateEntryPoint().execute(args)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "sam:handpicked",
            "--records",
            "0,1,2,3,4,284,335,592,675,719",
            "stp:n",
            "0",
            "start",
            "--dataset",
            dataset,
            str(p2),
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0

    dataset = "benchmark:van_de_Schoot_2017"
    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"

        # run
        with unittest.mock.patch(
            "asreview.entry_points.simulate.ReviewSimulate",
            autospec=True,
            return_value=None
        ):
            try:
                run_asreview_simulate_cli()
            except:
                args1 = asreview.entry_points.simulate.ReviewSimulate
        with unittest.mock.patch(
            "asreview_simulation.cli.terminators._start.ReviewSimulate",
            autospec=True,
            return_value=None
        ):
            try:
                run_asreview_simulation_start_cli()
            except:
                args2 = asreview_simulation.cli.terminators._start.ReviewSimulate

            # compare the two results
            # TODO
            assert args1 == args2