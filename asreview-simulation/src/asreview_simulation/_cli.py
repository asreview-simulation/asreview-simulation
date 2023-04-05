import click

from importlib.metadata import entry_points as entrypoints
from .balancers import double_balancer
from .balancers import none_balancer
from .balancers import triple_balancer
from .balancers import undersample_balancer
from .classifiers import naive_bayes_classifier
from .classifiers import random_forest_classifier
from .classifiers import logistic_classifier
from .classifiers import lstm_base_classifier
from .classifiers import lstm_pool_classifier
from .classifiers import nn_2_layer_classifier
from .classifiers import svm_classifier
from .extractors import doc2vec_extractor
from .extractors import tfidf_extractor
from .extractors import embedding_idf_extractor
from .extractors import embedding_lstm_extractor
from .extractors import sbert_extractor
from .samplers import random_prior_sampler
from .samplers import handpicked_prior_sampler
from .queriers import cluster_querier
from .queriers import mixed_querier
from .starters import load_settings
from .terminators import print_settings
from .terminators import save_settings
from .terminators import start
from ._state import State


class NaturalOrderGroup(click.Group):
    # thanks https://github.com/pallets/click/issues/513#issuecomment-504158316
    def list_commands(self, ctx):
        return self.commands.keys()


def _add_balancer_subcommands():
    my_balancers = [
        double_balancer,
        none_balancer,
        triple_balancer,
        undersample_balancer
    ]
    try:
        other_balancers = [e.load() for e in entrypoints(group="asreview_simulation.balancers")]
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreview_simulation.balancers'. The error message was: {e}\nContinuing...")
        other_balancers = []
    for b in _sort_commands(my_balancers + other_balancers):
        cli.add_command(b)


def _add_classifier_subcommands():
    my_classifiers = [
        naive_bayes_classifier,
        random_forest_classifier,
        logistic_classifier,
        lstm_base_classifier,
        lstm_pool_classifier,
        nn_2_layer_classifier,
        svm_classifier
    ]
    try:
        other_classifiers = [e.load() for e in entrypoints(group="asreview_simulation.classifiers")]
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreview_simulation.classifiers'. The error message was: {e}\nContinuing...")
        other_classifiers = []
    for c in _sort_commands(my_classifiers + other_classifiers):
        cli.add_command(c)


def _add_extractor_subcommands():
    my_extractors = [
        doc2vec_extractor,
        tfidf_extractor,
        embedding_idf_extractor,
        embedding_lstm_extractor,
        sbert_extractor
    ]
    try:
        other_extractors = [e.load() for e in entrypoints(group="asreview_simulation.extractors")]
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreview_simulation.extractors'. The error message was: {e}\nContinuing...")
        other_extractors = []
    for e in _sort_commands(my_extractors + other_extractors):
        cli.add_command(e)


def _add_querier_subcommands():
    my_queriers = [
        cluster_querier,
        mixed_querier
    ]
    try:
        other_queriers = [e.load() for e in entrypoints(group="asreview_simulation.queriers")]
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreview_simulation.queriers'. The error message was: {e}\nContinuing...")
        other_queriers = []
    for q in _sort_commands(my_queriers + other_queriers):
        cli.add_command(q)


def _add_sampler_subcommands():
    my_samplers = [
        random_prior_sampler,
        handpicked_prior_sampler
    ]
    try:
        other_samplers = [e.load() for e in entrypoints(group="asreview_simulation.samplers")]
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreview_simulation.samplers'. The error message was: {e}\nContinuing...")
        other_samplers = []
    for s in _sort_commands(my_samplers + other_samplers):
        cli.add_command(s)


def _add_starter_subcommands():
    my_starters = [
        load_settings
    ]
    try:
        other_starters = [e.load() for e in entrypoints(group="asreview_simulation.starters")]
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreview_simulation.starters'. The error message was: {e}\nContinuing...")
        other_starters = []
    for s in _sort_commands(my_starters + other_starters):
        cli.add_command(s)


def _add_terminator_subcommands():
    my_terminators = [
        print_settings,
        save_settings,
        start
    ]
    try:
        other_terminators = [e.load() for e in entrypoints(group="asreview_simulation.terminators")]
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreview_simulation.terminators'. The error message was: {e}\nContinuing...")
        other_terminators = []
    for t in _sort_commands(my_terminators + other_terminators):
        cli.add_command(t)


def _sort_commands(commands):
    return sorted(commands, key=lambda command: command.name)


def cli_help(cli_name="asreview-simulation"):
    return f"""
Example usage:

  $ {cli_name} print-settings

  $ {cli_name} start labeled-records.db

Commands can be chained together, e.g.


  $ {cli_name} load-config thefile.cfg start labeled-records.db

  $ {cli_name} bal:double --alpha 1.23 print-settings --pretty

  $ {cli_name} bal:none c-nb e-tfidf q-mixed start labeled-records.db

\b
  $ {cli_name} sam:random --n_included 10 --n_excluded 15                      \\
    {' ' * len(cli_name)} ext:tfidf --ngram_max 2                                         \\
    {' ' * len(cli_name)} cls:nb --alpha 3.823                                            \\
    {' ' * len(cli_name)} qer:mixed --strategy1 max --strategy2 random --mix_ratio 0.95   \\
    {' ' * len(cli_name)} bal:double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1           \\
    {' ' * len(cli_name)} start labeled-records.db

Chained commands are evaluated left to right; make sure to end the chain with
either a 'start' command or a 'print-settings' command, otherwise it may appear
like nothing is happening.
"""


@click.group("cli",
             chain=True,
             cls=NaturalOrderGroup,
             context_settings={"help_option_names": ["-h", "--help"]},
             help=cli_help())
@click.pass_context
def cli(ctx):
    if ctx.obj is None:
        ctx.obj = State()


_add_starter_subcommands()
_add_sampler_subcommands()
_add_balancer_subcommands()
_add_classifier_subcommands()
_add_extractor_subcommands()
_add_querier_subcommands()
_add_terminator_subcommands()
