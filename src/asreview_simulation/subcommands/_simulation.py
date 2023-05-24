from .._cli import cli
from .._cli import cli_help
from asreview.subcommands import BaseSubcommand


class SimulationSubcommand(BaseSubcommand):
    """Simulation"""

    description = "Simulate labeling records using different models and parameterizations."

    def __init__(self):
        self.version = "simulation"

    def __call__(self, argv):
        name = "asreview simulation"
        cli.help = cli_help(name)
        cli(argv, prog_name=name)
