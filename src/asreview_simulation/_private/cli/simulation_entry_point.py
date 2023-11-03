from asreview.entry_points import BaseEntryPoint
from asreview_simulation._private.cli.cli import cli
from asreview_simulation._private.cli.cli import cli_help


class SimulationEntryPoint(BaseEntryPoint):
    """Simulation"""

    description = "Simulate labeling records using different models and parameterizations."

    def __init__(self):
        self.version = "simulation"

    def execute(self, argv):
        name = "asreview simulation"
        cli.help = cli_help(name)
        cli(argv, prog_name=name)
