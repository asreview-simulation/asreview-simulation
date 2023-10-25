import unittest.mock
from pathlib import Path
from tempfile import TemporaryDirectory
import asreview
import pytest
from asreview import get_data_home
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
import asreview_simulation
from asreview_simulation.cli import cli
from tests.helpers import compare_arguments_mock
from tests.helpers import get_model_combinatorics
from tests.helpers import get_xfails_mocked


def test_minimal_args():
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
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
            "start",
            "--benchmark",
            benchmark,
            "--out",
            str(p2),
        ]
        with unittest.mock.patch(mocked2, autospec=True, return_value=None):
            runner.invoke(cli, args)
            return asreview_simulation.cli.terminators._start.ReviewSimulate.call_args

    benchmark = "benchmark:van_de_Schoot_2017"
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
    - use mocked instance of ReviewSimulate to monitor how it's called
    """

    def run_asreview_simulate_cli():
        embedding_pars = list()
        if fex == "embedding-lstm":
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
            "max",
            "-b",
            "double",
            "-e",
            fex,
            *embedding_pars,
            "--seed",
            "567",
            "--stop_if",
            "5",
            "--n_instances",
            "20",
            benchmark,
        ]
        with unittest.mock.patch(mocked1, autospec=True, return_value=None):
            try:
                SimulateEntryPoint().execute(args)
            except Exception:
                return asreview.entry_points.simulate.ReviewSimulate.call_args

    def run_asreview_simulation_start_cli():
        embedding_pars = list()
        if fex == "embedding-lstm":
            embedding_pars += ["--embedding"]
            embedding_pars += [str(get_data_home() / "fasttext.cc.en.300.vec")]
        args = [
            "sam-random",
            "--init_seed",
            "42",
            "--n_included",
            "5",
            "--n_excluded",
            "5",
            f"bal-double",
            f"cls-{cls}",
            f"fex-{fex}",
            *embedding_pars,
            f"qry-max",
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
        ]
        runner = CliRunner()
        with unittest.mock.patch(mocked2, autospec=True, return_value=None):
            runner.invoke(cli, args)
            return asreview_simulation.cli.terminators._start.ReviewSimulate.call_args

    xfail, reason = get_xfails_mocked(parameterization)
    if xfail:
        pytest.xfail(reason=reason)

    benchmark = "benchmark:van_de_Schoot_2017"
    fex, cls = parameterization.split(",")

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
