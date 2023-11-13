import unittest.mock
from pathlib import Path
from tempfile import TemporaryDirectory
import asreview
import pytest
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
import asreview_simulation
from asreview_simulation._private.cli.cli import cli
from tests.helpers.compare_arguments_mock import compare_arguments_mock


@pytest.mark.sam_handpicked
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_nq
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
        with unittest.mock.patch(mocked1, autospec=True, return_value=None):
            try:
                SimulateEntryPoint().execute(args)
            except Exception:
                return asreview.entry_points.simulate.ReviewSimulate.call_args

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
        ]
        with unittest.mock.patch(mocked2, autospec=True, return_value=None):
            runner.invoke(cli, args)
            return asreview_simulation._private.lib.run.ReviewSimulate.call_args

    benchmark = "benchmark:van_de_Schoot_2017"
    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"
        mocked1 = "asreview.entry_points.simulate.ReviewSimulate"
        mocked2 = "asreview_simulation._private.lib.run.ReviewSimulate"

        # run
        args1, kwargs1 = run_asreview_simulate_cli()
        args2, kwargs2 = run_asreview_simulation_start_cli()

        # compare the two results
        compare_arguments_mock(args1, kwargs1, args2, kwargs2, tmpdir)


@pytest.mark.sam_handpicked
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_nq
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
        with unittest.mock.patch(mocked1, autospec=True, return_value=None):
            try:
                SimulateEntryPoint().execute(args)
            except Exception:
                return asreview.entry_points.simulate.ReviewSimulate.call_args

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
        ]
        with unittest.mock.patch(mocked2, autospec=True, return_value=None):
            runner.invoke(cli, args)
            return asreview_simulation._private.lib.run.ReviewSimulate.call_args

    benchmark = "benchmark:van_de_Schoot_2017"
    with TemporaryDirectory(prefix="pytest.") as tmpdir:
        # prep
        p1 = Path(tmpdir) / "simulate.asreview"
        p2 = Path(tmpdir) / "simulation.asreview"
        mocked1 = "asreview.entry_points.simulate.ReviewSimulate"
        mocked2 = "asreview_simulation._private.lib.run.ReviewSimulate"

        # run
        args1, kwargs1 = run_asreview_simulate_cli()
        args2, kwargs2 = run_asreview_simulation_start_cli()

        # compare the two results
        compare_arguments_mock(args1, kwargs1, args2, kwargs2, tmpdir)
