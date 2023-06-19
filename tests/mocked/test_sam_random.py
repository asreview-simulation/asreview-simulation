from pathlib import Path
from tempfile import TemporaryDirectory
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
from asreview_simulation.cli import cli
import asreview
import asreview_simulation
import unittest.mock
from tests.helpers import compare_arguments_mock


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
            dataset,
        ]
        with unittest.mock.patch(mocked1, autospec=True, return_value=None):
            try:
                SimulateEntryPoint().execute(args)
            except Exception:
                return asreview.entry_points.simulate.ReviewSimulate.call_args

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
            "stp:n",
            "0",
            "start",
            "--dataset",
            dataset,
            str(p2),
        ]
        with unittest.mock.patch(mocked2, autospec=True, return_value=None):
            runner.invoke(cli, args)
            return asreview_simulation.cli.terminators._start.ReviewSimulate.call_args

    dataset = "benchmark:van_de_Schoot_2017"
    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"
        mocked1 = "asreview.entry_points.simulate.ReviewSimulate"
        mocked2 = "asreview_simulation.cli.terminators._start.ReviewSimulate"

        # run
        args1, kwargs1 = run_asreview_simulate_cli()
        args2, kwargs2 = run_asreview_simulation_start_cli()

        # compare the two results
        compare_arguments_mock(args1, kwargs1, args2, kwargs2, tmpdir)
