from .._cli import cli
from asreview.subcommands import BaseSubcommand


class LabSubcommand(BaseSubcommand):
    """Lab"""

    description = "Start ASReview LAB"

    def __init__(self):
        self.version = "lab"

    def __call__(self, argv):
        name = "asreview lab"
        cli(argv, prog_name=name)
