from pathlib import Path
from tempfile import TemporaryDirectory
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
from asreview_simulation.cli import cli
import asreview
import asreview_simulation
import unittest.mock
from tests.helpers import compare_arguments_mock
from tests.helpers import get_model_combinatorics
import pytest
from asreview import get_data_home


def test_minimal_args():
    def run_asreview_simulate_cli():
        args = [
            "--state_file",
            str(p1),
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


@pytest.mark.parametrize("parameterization", get_model_combinatorics())
def test_with_model_combinations(parameterization):
    """
    - seeded random prior with 5 included and 5 excluded
    - generate 20 instances in each query
    - stop querying after 5 queries for a total of 110 records
    - use one dataset, benchmark:van_de_Schoot_2017
    - try different combinations of balancer, classifier, extractor, querier
    - use default parameterization for each model
    - use mocked instance of ReviewSimulate to monitor how it's called
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
        with unittest.mock.patch(mocked1, autospec=True, return_value=None):
            try:
                SimulateEntryPoint().execute(args)
            except Exception:
                return asreview.entry_points.simulate.ReviewSimulate.call_args

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
        with unittest.mock.patch(mocked2, autospec=True, return_value=None):
            runner.invoke(cli, args)
            return asreview_simulation.cli.terminators._start.ReviewSimulate.call_args

    dataset = "benchmark:van_de_Schoot_2017"
    bal, cls, fex, qry = parameterization.split(",")
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
