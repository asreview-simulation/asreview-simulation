import os
from tempfile import TemporaryDirectory
from asreview.entry_points import SimulateEntryPoint
from click.testing import CliRunner
from asreview_simulation import cli


def test_simulate_start():
    def run_asreview_simulate_cli():
        args = [
            dataset,
            "--state_file", os.path.join(d, "simulate.asreview")
        ]
        SimulateEntryPoint().execute(args)

    def run_asreview_simulation_start_cli():
        runner = CliRunner()
        args = [
            "start",
            "--dataset", dataset,
            os.path.join(d, "simulation.asreview")
        ]
        result = runner.invoke(cli, args)
        assert result.exit_code == 0

    dataset = "benchmark:van_de_Schoot_2017"
    with TemporaryDirectory(prefix="pytest.") as d:
        run_asreview_simulate_cli()
        run_asreview_simulation_start_cli()
        print()

    # compare the two results
