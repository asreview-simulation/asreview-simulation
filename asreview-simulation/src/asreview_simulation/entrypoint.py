from ._cli import cli
from ._cli import cli_help
from asreview.entry_points import BaseEntryPoint


class SimulationEntrypoint(BaseEntryPoint):
    """Simulation"""

    description = "Simulate labeling records using different models and parameterizations."

    def __init__(self):
        self.version = "plugin-simulation"

    def execute(self, argv):
        name = "asreview simulation"
        cli.help = cli_help(name)
        cli(argv, prog_name=name)
