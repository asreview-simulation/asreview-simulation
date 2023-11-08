import unittest.mock
from pathlib import Path
from tempfile import TemporaryDirectory
import asreview
import pytest
from asreview import get_data_home
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
import asreview_simulation
from asreview_simulation._private.cli import cli
from tests.helpers.compare_arguments_mock import compare_arguments_mock
from tests.helpers.get_model_combinatorics import get_model_combinatorics
from tests.helpers.get_xfails_mocked import get_xfails_mocked


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
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


@pytest.mark.sam_random
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_nq
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
            cls,
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
        with unittest.mock.patch(mocked1, autospec=True, return_value=None):
            try:
                SimulateEntryPoint().execute(args)
            except Exception:
                return asreview.entry_points.simulate.ReviewSimulate.call_args

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
            f"cls-{cls}",
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
        ]
        runner = CliRunner()
        with unittest.mock.patch(mocked2, autospec=True, return_value=None):
            runner.invoke(cli, args)
            return asreview_simulation._private.lib.run.ReviewSimulate.call_args

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
        mocked2 = "asreview_simulation._private.lib.run.ReviewSimulate"

        # run
        args1, kwargs1 = run_asreview_simulate_cli()
        args2, kwargs2 = run_asreview_simulation_start_cli()

        # compare the two results
        compare_arguments_mock(args1, kwargs1, args2, kwargs2, tmpdir)
