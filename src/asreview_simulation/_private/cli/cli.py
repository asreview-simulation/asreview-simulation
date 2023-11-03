import os
from importlib.metadata import entry_points as entrypoints
import click
from asreview_simulation._private.cli.balancers.double import bal_double
from asreview_simulation._private.cli.balancers.simple import bal_simple
from asreview_simulation._private.cli.balancers.undersample import bal_undersample
from asreview_simulation._private.cli.classifiers.logistic import cls_logistic
from asreview_simulation._private.cli.classifiers.lstm_base import cls_lstm_base
from asreview_simulation._private.cli.classifiers.lstm_pool import cls_lstm_pool
from asreview_simulation._private.cli.classifiers.nb import cls_nb
from asreview_simulation._private.cli.classifiers.nn_2_layer import cls_nn_2_layer
from asreview_simulation._private.cli.classifiers.rf import cls_rf
from asreview_simulation._private.cli.classifiers.svm import cls_svm
from asreview_simulation._private.cli.extractors.doc2vec import fex_doc2vec
from asreview_simulation._private.cli.extractors.embedding_idf import fex_embedding_idf
from asreview_simulation._private.cli.extractors.embedding_lstm import fex_embedding_lstm
from asreview_simulation._private.cli.extractors.sbert import fex_sbert
from asreview_simulation._private.cli.extractors.tfidf import fex_tfidf
from asreview_simulation._private.cli.queriers.cluster import qry_cluster
from asreview_simulation._private.cli.queriers.max import qry_max
from asreview_simulation._private.cli.queriers.max_random import qry_max_random
from asreview_simulation._private.cli.queriers.max_uncertainty import qry_max_uncertainty
from asreview_simulation._private.cli.queriers.random import qry_random
from asreview_simulation._private.cli.queriers.uncertainty import qry_uncertainty
from asreview_simulation._private.cli.samplers.handpicked import sam_handpicked
from asreview_simulation._private.cli.samplers.random import sam_random
from asreview_simulation._private.cli.starters.load_settings import load_settings
from asreview_simulation._private.cli.state import State
from asreview_simulation._private.cli.stopping.none import stp_none
from asreview_simulation._private.cli.stopping.nq import stp_nq
from asreview_simulation._private.cli.stopping.rel import stp_rel
from asreview_simulation._private.cli.terminators.print_benchmark_names import print_benchmark_names
from asreview_simulation._private.cli.terminators.print_settings import print_settings
from asreview_simulation._private.cli.terminators.save_settings import save_settings
from asreview_simulation._private.cli.terminators.start import start


class NaturalOrderGroup(click.Group):
    # thanks https://github.com/pallets/click/issues/513#issuecomment-504158316
    def list_commands(self, ctx):
        return self.commands.keys()


def _add_balancer_subcommands():
    my_balancers = [
        bal_double,
        bal_simple,
        bal_undersample,
    ]
    try:
        other_balancers = [e.load() for e in entrypoints(group="asreview_simulation.balancers")]
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
        cls_nb,
        cls_rf,
        cls_logistic,
        cls_lstm_base,
        cls_lstm_pool,
        cls_nn_2_layer,
        cls_svm,
    ]
    try:
        other_classifiers = [e.load() for e in entrypoints(group="asreview_simulation.classifiers")]
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
        fex_doc2vec,
        fex_tfidf,
        fex_embedding_idf,
        fex_embedding_lstm,
        fex_sbert,
    ]
    try:
        other_extractors = [e.load() for e in entrypoints(group="asreview_simulation.extractors")]
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
        qry_cluster,
        qry_max,
        qry_max_random,
        qry_max_uncertainty,
        qry_random,
        qry_uncertainty,
    ]
    try:
        other_queriers = [e.load() for e in entrypoints(group="asreview_simulation.queriers")]
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
        sam_random,
        sam_handpicked,
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
        stp_nq,
        stp_none,
        stp_rel,
    ]
    for t in _sort_commands(my_stopping):
        cli.add_command(t)


def _add_terminator_subcommands():
    my_terminators = [
        start,
        print_benchmark_names,
        print_settings,
        save_settings,
    ]
    for t in my_terminators:
        cli.add_command(t)


def _sort_commands(commands):
    return sorted(commands, key=lambda command: command.name)


def cli_help(cli_name="asreview-simulation"):
    return f"""
Command line interface to simulate an ASReview analysis using a variety of prior sampling strategies,
classifiers, feature extractors, queriers, balancers, and stopping rules -- all of which can be configured
to run with custom parameterizations.

Printing this help:

$ {cli_name} --help

Printing the configuration:

$ {cli_name} print-settings

Starting a simulation using the default combination of models (sam-random, bal-double, cls-nb, fex-tfidf,
qry-max, stp-rel), each using its default parameterization:

\b
$ {cli_name} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

Instead of a benchmark dataset, you can also supply your own data via the `--in` option, as follows:

$ {cli_name} start --in .{os.sep}myfile.csv --out .{os.sep}project.asreview

$ {cli_name} start --in .{os.sep}myfile.ris --out .{os.sep}project.asreview

$ {cli_name} start --in .{os.sep}myfile.tsv --out .{os.sep}project.asreview

$ {cli_name} start --in .{os.sep}myfile.xlsx --out .{os.sep}project.asreview

Using a different classifier strategy can be accomplished by using one of the 'cls-*' subcommands
before issuing the 'start' subcommand, e.g.:

\b
$ {cli_name} cls-logistic \\
  {' ' * len(cli_name)} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

Subcommands can be chained together, for example using the logistic classifier with
the undersample balancer goes like this:

\b
$ {cli_name} cls-logistic \\
  {' ' * len(cli_name)} bal-undersample \\
  {' ' * len(cli_name)} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

Most subcommands have their own parameterization. Check the help of a subcommand with --help or -h for short, e.g.:

$ {cli_name} cls-logistic --help

Passing parameters to a subcommand goes like this:

\b
$ {cli_name} cls-logistic --class_weight 1.1 \\
  {' ' * len(cli_name)} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

By chaining individually parameterized subcommands, we can compose a variety of configurations, e.g.:

\b
$ {cli_name} sam-random --n_included 10 --n_excluded 15 \\
  {' ' * len(cli_name)} fex-tfidf --ngram_max 2 \\
  {' ' * len(cli_name)} cls-nb --alpha 3.823 \\
  {' ' * len(cli_name)} qry-max-random --mix_ratio 0.95 --n_instances 10 \\
  {' ' * len(cli_name)} bal-double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1 \\
  {' ' * len(cli_name)} stp-nq --n_queries 20 \\
  {' ' * len(cli_name)} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

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
