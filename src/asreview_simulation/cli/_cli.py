import os
from importlib.metadata import entry_points as entrypoints
import click
from ._state import State
from .balancers import double_balancer
from .balancers import simple_balancer
from .balancers import undersample_balancer
from .classifiers import logistic_classifier
from .classifiers import lstm_base_classifier
from .classifiers import lstm_pool_classifier
from .classifiers import naive_bayes_classifier
from .classifiers import nn_2_layer_classifier
from .classifiers import random_forest_classifier
from .classifiers import svm_classifier
from .extractors import doc2vec_extractor
from .extractors import embedding_idf_extractor
from .extractors import embedding_lstm_extractor
from .extractors import sbert_extractor
from .extractors import tfidf_extractor
from .queriers import cluster_querier
from .queriers import max_querier
from .queriers import max_random_querier
from .queriers import max_uncertainty_querier
from .queriers import random_querier
from .queriers import uncertainty_querier
from .samplers import handpicked_prior_sampler
from .samplers import random_prior_sampler
from .starters import load_settings
from .stopping import min_stopping
from .stopping import none_stopping
from .stopping import nq_stopping
from .terminators import print_benchmark_names
from .terminators import print_settings
from .terminators import save_settings
from .terminators import start


class NaturalOrderGroup(click.Group):
    # thanks https://github.com/pallets/click/issues/513#issuecomment-504158316
    def list_commands(self, ctx):
        return self.commands.keys()


def _add_balancer_subcommands():
    my_balancers = [
        double_balancer,
        simple_balancer,
        undersample_balancer,
    ]
    try:
        other_balancers = [
            e.load() for e in entrypoints(group="asreview_simulation.balancers")
        ]
    except Exception as e:
        print(
            "Something went wrong loading a module from entrypoint group "
            + f"'asreview_simulation.balancers'. The error message was: {e}\nContinuing..."
        )
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
        svm_classifier,
    ]
    try:
        other_classifiers = [
            e.load() for e in entrypoints(group="asreview_simulation.classifiers")
        ]
    except Exception as e:
        print(
            "Something went wrong loading a module from entrypoint group "
            + f"'asreview_simulation.classifiers'. The error message was: {e}\nContinuing..."
        )
        other_classifiers = []
    for c in _sort_commands(my_classifiers + other_classifiers):
        cli.add_command(c)


def _add_extractor_subcommands():
    my_extractors = [
        doc2vec_extractor,
        tfidf_extractor,
        embedding_idf_extractor,
        embedding_lstm_extractor,
        sbert_extractor,
    ]
    try:
        other_extractors = [
            e.load() for e in entrypoints(group="asreview_simulation.extractors")
        ]
    except Exception as e:
        print(
            "Something went wrong loading a module from entrypoint group "
            + f"'asreview_simulation.extractors'. The error message was: {e}\nContinuing..."
        )
        other_extractors = []
    for e in _sort_commands(my_extractors + other_extractors):
        cli.add_command(e)


def _add_querier_subcommands():
    my_queriers = [
        cluster_querier,
        max_querier,
        max_random_querier,
        max_uncertainty_querier,
        random_querier,
        uncertainty_querier,
    ]
    try:
        other_queriers = [
            e.load() for e in entrypoints(group="asreview_simulation.queriers")
        ]
    except Exception as e:
        print(
            "Something went wrong loading a module from entrypoint group "
            + f"'asreview_simulation.queriers'. The error message was: {e}\nContinuing..."
        )
        other_queriers = []
    for q in _sort_commands(my_queriers + other_queriers):
        cli.add_command(q)


def _add_sampler_subcommands():
    my_samplers = [
        random_prior_sampler,
        handpicked_prior_sampler,
    ]
    for s in _sort_commands(my_samplers):
        cli.add_command(s)


def _add_starter_subcommands():
    my_starters = [
        load_settings,
    ]
    for s in _sort_commands(my_starters):
        cli.add_command(s)


def _add_stopping_subcommands():
    my_stopping = [
        min_stopping,
        nq_stopping,
        none_stopping,
    ]
    for t in _sort_commands(my_stopping):
        cli.add_command(t)


def _add_terminator_subcommands():
    my_terminators = [
        start,
        print_benchmark_names,
        print_settings,
        save_settings
    ]
    for t in my_terminators:
        cli.add_command(t)


def _sort_commands(commands):
    return sorted(commands, key=lambda command: command.name)


def cli_help(cli_name="asreview-simulation"):
    return f"""
Command line interface to simulate an ASReview analysis using a variety of classifiers, feature
extractors, queriers, and balancers, which can all be configured to run with custom parameterizations.

Printing this help:

$ {cli_name} --help

Printing the configuration:

$ {cli_name} print-settings

Starting a simulation using the default combination of models (sam-random, bal-double, cls-nb, fex-tfidf,
qry-max, stp-min), each using its default parameterization:

$ {cli_name} start --benchmark benchmark:van_de_Schoot_2017 --out .{os.sep}project.asreview

Instead of a benchmark dataset, you can also supply your own data via the `--in` option, as follows:

$ {cli_name} start --in .{os.sep}myfile.csv --out .{os.sep}project.asreview

$ {cli_name} start --in .{os.sep}myfile.ris --out .{os.sep}project.asreview

$ {cli_name} start --in .{os.sep}myfile.tsv --out .{os.sep}project.asreview

$ {cli_name} start --in .{os.sep}myfile.xlsx --out .{os.sep}project.asreview

Using a different classifier strategy can be accomplished by using one of the 'cls-*' subcommands
before issuing the 'start' subcommand, e.g.:

$ {cli_name} cls-logistic start --benchmark benchmark:van_de_Schoot_2017 --out .{os.sep}project.asreview

Subcommands can be chained together, for example using the logistic classifier with
the undersample balancer goes like this:

$ {cli_name} cls-logistic bal-undersample start --benchmark benchmark:van_de_Schoot_2017 --out .{os.sep}project.asreview

Most subcommands have their own parameterization. Check the help of a subcommand with --help or -h for short, e.g.:

$ {cli_name} cls-logistic --help

Passing parameters to a subcommand goes like this:

$ {cli_name} cls-logistic --class_weight 1.1 start --benchmark benchmark:van_de_Schoot_2017 --out .{os.sep}project.asreview

By chaining individually parameterized subcommands, we can compose a variety of configurations, e.g.:

\b
$ {cli_name} sam-random --n_included 10 --n_excluded 15            \\
  {' ' * len(cli_name)} fex-tfidf --ngram_max 2                               \\
  {' ' * len(cli_name)} cls-nb --alpha 3.823                                  \\
  {' ' * len(cli_name)} qry-max-random --mix_ratio 0.95 --n_instances 10      \\
  {' ' * len(cli_name)} bal-double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1 \\
  {' ' * len(cli_name)} stp-nq --n_queries 20                                 \\
  {' ' * len(cli_name)} start --benchmark benchmark:van_de_Schoot_2017 --out .{os.sep}project.asreview

Chained commands are evaluated left to right; make sure to end the chain with
the 'start' command, otherwise it may appear like nothing is happening.

Please report any issues at:

https://github.com/asreview-tuning/asreview-simulation/issues.
"""


@click.group(
    "cli",
    chain=True,
    cls=NaturalOrderGroup,
    context_settings={"help_option_names": ["-h", "--help"]},
    help=cli_help(),
)
@click.pass_context
def cli(ctx):
    if ctx.obj is None:
        ctx.obj = State()


_add_terminator_subcommands()
_add_starter_subcommands()
_add_sampler_subcommands()
_add_extractor_subcommands()
_add_classifier_subcommands()
_add_querier_subcommands()
_add_balancer_subcommands()
_add_stopping_subcommands()
