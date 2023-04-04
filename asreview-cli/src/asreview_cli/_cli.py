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
from .starters import load_config
from .terminators import print_settings
from .terminators import start
from ._state import State


def _add_balancer_subcommands():
    my_balancers = [
        double_balancer,
        none_balancer,
        triple_balancer,
        undersample_balancer
    ]
    other_balancers = [e.load() for e in entrypoints(group="asreview_cli.balancers")]
    for b in my_balancers + other_balancers:
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
    other_classifiers = [e.load() for e in entrypoints(group="asreview_cli.classifiers")]
    for c in my_classifiers + other_classifiers:
        cli.add_command(c)


def _add_extractor_subcommands():
    my_extractors = [
        doc2vec_extractor,
        tfidf_extractor,
        embedding_idf_extractor,
        embedding_lstm_extractor,
        sbert_extractor
    ]
    other_extractors = [e.load() for e in entrypoints(group="asreview_cli.extractors")]
    for e in my_extractors + other_extractors:
        cli.add_command(e)


def _add_querier_subcommands():
    my_queriers = [
        cluster_querier,
        mixed_querier
    ]
    other_queriers = [e.load() for e in entrypoints(group="asreview_cli.queriers")]
    for q in my_queriers + other_queriers:
        cli.add_command(q)


def _add_sampler_subcommands():
    my_samplers = [
        random_prior_sampler,
        handpicked_prior_sampler
    ]
    other_samplers = [e.load() for e in entrypoints(group="asreview_cli.samplers")]
    for s in my_samplers + other_samplers:
        cli.add_command(s)


def _add_starter_subcommands():
    my_starters = [
        load_config
    ]
    other_starters = [e.load() for e in entrypoints(group="asreview_cli.starters")]
    for s in my_starters + other_starters:
        cli.add_command(s)


def _add_terminator_subcommands():
    my_terminators = [
        print_settings,
        start
    ]
    other_terminators = [e.load() for e in entrypoints(group="asreview_cli.terminators")]
    for t in my_terminators + other_terminators:
        cli.add_command(t)


def cli_help(cli_name="asreview-cli"):
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
either a 'start' command or a 'print-settings' command, otherwise it appears
like nothing is happening.
"""


@click.group("cli",
             chain=True,
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
