import unittest.mock
from pathlib import Path
from tempfile import TemporaryDirectory
import asreview
import pytest
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
import asreviewcontrib
from asreviewcontrib.simulation._private.cli.cli import cli
from tests.helpers.compare_arguments_mock import compare_arguments_mock


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.clr_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_nq
def test_with_init_seed():
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
            "--init_seed",
            "420",
            "--n_prior_included",
            "5",
            "--n_prior_excluded",
            "5",
            "--stop_if",
            "0",
            benchmark,
        ]
        with unittest.mock.patch(mocked1, autospec=True, return_value=None):
            try:
                SimulateEntryPoint().execute(args)
            except Exception:
                return asreview.entry_points.simulate.ReviewSimulate.call_args

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "sam-random",
            "--n_included",
            "5",
            "--n_excluded",
            "5",
            "--seed",
            "420",
            "stp-nq",
            "--n_queries",
            "0",
            "start",
            "--benchmark",
            benchmark,
            "--out",
            str(p2),
        ]
        with unittest.mock.patch(mocked2, autospec=True, return_value=None):
            runner.invoke(cli, args)
            return asreviewcontrib.simulation._private.lib.run.ReviewSimulate.call_args

    benchmark = "benchmark:van_de_Schoot_2017"
    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"
        mocked1 = "asreview.entry_points.simulate.ReviewSimulate"
        mocked2 = "asreviewcontrib.simulation._private.lib.run.ReviewSimulate"

        # run
        args1, kwargs1 = run_asreview_simulate_cli()
        args2, kwargs2 = run_asreview_simulation_start_cli()

        # compare the two results
        compare_arguments_mock(args1, kwargs1, args2, kwargs2, tmpdir)
