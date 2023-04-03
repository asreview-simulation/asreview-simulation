from ._cli import cli
from ._cli import cli_help
from asreview.entry_points import BaseEntryPoint


class SimulateEntrypoint(BaseEntryPoint):
    """Simulation"""

    description = "Simulate labeling records using different models and parameterizations."

    def __init__(self):
        self.version = "simulation-cli-plugin"

    def execute(self, argv):
        name = "asreview simulation"
        cli.help = cli_help(name)
        cli(argv, prog_name=name)
