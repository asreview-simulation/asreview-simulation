import click

from .balancer import double
from .balancer import simple
from .balancer import triple
from .balancer import undersample
from .classifier import naive_bayes
from .classifier import random_forest
from ._print_settings import print_settings
from ._simulate import simulate
from ._state import State


@click.group("cli", chain=True)
@click.pass_context
def group(ctx):
    if ctx.obj is None:
        ctx.obj = State()


group.add_command(double)
group.add_command(simple)
group.add_command(triple)
group.add_command(undersample)
group.add_command(naive_bayes)
group.add_command(random_forest)
group.add_command(print_settings)
group.add_command(simulate)
