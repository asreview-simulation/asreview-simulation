import os
from importlib.metadata import entry_points as entrypoints
import click
from asreviewcontrib.simulation._private.cli.bal_double_subcommand import bal_double_subcommand
from asreviewcontrib.simulation._private.cli.bal_simple_subcommand import bal_simple_subcommand
from asreviewcontrib.simulation._private.cli.bal_undersample_subcommand import bal_undersample_subcommand
from asreviewcontrib.simulation._private.cli.cli_state import State
from asreviewcontrib.simulation._private.cli.clr_logistic_subcommand import clr_logistic_subcommand
from asreviewcontrib.simulation._private.cli.clr_lstm_base_subcommand import clr_lstm_base_subcommand
from asreviewcontrib.simulation._private.cli.clr_lstm_pool_subcommand import clr_lstm_pool_subcommand
from asreviewcontrib.simulation._private.cli.clr_nb_subcommand import clr_nb_subcommand
from asreviewcontrib.simulation._private.cli.clr_nn_2_layer_subcommand import clr_nn_2_layer_subcommand
from asreviewcontrib.simulation._private.cli.clr_rf_subcommand import clr_rf_subcommand
from asreviewcontrib.simulation._private.cli.clr_svm_subcommand import clr_svm_subcommand
from asreviewcontrib.simulation._private.cli.fex_doc2vec_subcommand import fex_doc2vec_subcommand
from asreviewcontrib.simulation._private.cli.fex_embedding_idf_subcommand import fex_embedding_idf_subcommand
from asreviewcontrib.simulation._private.cli.fex_embedding_lstm_subcommand import fex_embedding_lstm_subcommand
from asreviewcontrib.simulation._private.cli.fex_sbert_subcommand import fex_sbert_subcommand
from asreviewcontrib.simulation._private.cli.fex_tfidf_subcommand import fex_tfidf_subcommand
from asreviewcontrib.simulation._private.cli.load_settings_subcommand import load_settings_subcommand
from asreviewcontrib.simulation._private.cli.ofn_none_subcommand import ofn_none_subcommand
from asreviewcontrib.simulation._private.cli.ofn_wss_subcommand import ofn_wss_subcommand
from asreviewcontrib.simulation._private.cli.print_benchmark_names_subcommand import print_benchmark_names_subcommand
from asreviewcontrib.simulation._private.cli.print_settings_subcommand import print_settings_subcommand
from asreviewcontrib.simulation._private.cli.qry_cluster_subcommand import qry_cluster_subcommand
from asreviewcontrib.simulation._private.cli.qry_max_random_subcommand import qry_max_random_subcommand
from asreviewcontrib.simulation._private.cli.qry_max_subcommand import qry_max_subcommand
from asreviewcontrib.simulation._private.cli.qry_max_uncertainty_subcommand import qry_max_uncertainty_subcommand
from asreviewcontrib.simulation._private.cli.qry_random_subcommand import qry_random_subcommand
from asreviewcontrib.simulation._private.cli.qry_uncertainty_subcommand import qry_uncertainty_subcommand
from asreviewcontrib.simulation._private.cli.sam_handpicked_subcommand import sam_handpicked_subcommand
from asreviewcontrib.simulation._private.cli.sam_random_subcommand import sam_random_subcommand
from asreviewcontrib.simulation._private.cli.save_settings_subcommand import save_settings_subcommand
from asreviewcontrib.simulation._private.cli.start_subcommand import start_subcommand
from asreviewcontrib.simulation._private.cli.stp_none_subcommand import stp_none_subcommand
from asreviewcontrib.simulation._private.cli.stp_nq_subcommand import stp_nq_subcommand
from asreviewcontrib.simulation._private.cli.stp_rel_subcommand import stp_rel_subcommand


class NaturalOrderGroup(click.Group):
    # thanks https://github.com/pallets/click/issues/513#issuecomment-504158316
    def list_commands(self, ctx):
        return self.commands.keys()


def add_bal_subcommands():
    my_bals = [
        bal_double_subcommand,
        bal_simple_subcommand,
        bal_undersample_subcommand,
    ]
    group = "asreviewcontrib.simulation.bal"
    try:
        other_bals = [e.load() for e in entrypoints(group=group)]
    except Exception as e:
        print(get_error_msg(group, e))
        other_bals = []
    for b in sort_commands(my_bals + other_bals):
        cli.add_command(b)


def add_clr_subcommands():
    my_clrs = [
        clr_nb_subcommand,
        clr_rf_subcommand,
        clr_logistic_subcommand,
        clr_lstm_base_subcommand,
        clr_lstm_pool_subcommand,
        clr_nn_2_layer_subcommand,
        clr_svm_subcommand,
    ]
    group = "asreviewcontrib.simulation.clr"
    try:
        other_clrs = [e.load() for e in entrypoints(group=group)]
    except Exception as e:
        print(get_error_msg(group, e))
        other_clrs = []
    for c in sort_commands(my_clrs + other_clrs):
        cli.add_command(c)


def add_fex_subcommands():
    my_fexs = [
        fex_doc2vec_subcommand,
        fex_tfidf_subcommand,
        fex_embedding_idf_subcommand,
        fex_embedding_lstm_subcommand,
        fex_sbert_subcommand,
    ]
    group = "asreviewcontrib.simulation.fex"
    try:
        other_fexs = [e.load() for e in entrypoints(group=group)]
    except Exception as e:
        print(get_error_msg(group, e))
        other_fexs = []
    for e in sort_commands(my_fexs + other_fexs):
        cli.add_command(e)


def add_ofn_subcommands():
    my_ofns = [
        ofn_none_subcommand,
        ofn_wss_subcommand,
    ]
    group = "asreviewcontrib.simulation.ofn"
    try:
        other_ofns = [e.load() for e in entrypoints(group=group)]
    except Exception as e:
        print(get_error_msg(group, e))
        other_ofns = []
    for o in sort_commands(my_ofns + other_ofns):
        cli.add_command(o)


def add_qry_subcommands():
    my_qrys = [
        qry_cluster_subcommand,
        qry_max_subcommand,
        qry_max_random_subcommand,
        qry_max_uncertainty_subcommand,
        qry_random_subcommand,
        qry_uncertainty_subcommand,
    ]
    group = "asreviewcontrib.simulation.qry"
    try:
        other_qrys = [e.load() for e in entrypoints(group=group)]
    except Exception as e:
        print(get_error_msg(group, e))
        other_qrys = []
    for q in sort_commands(my_qrys + other_qrys):
        cli.add_command(q)


def add_sam_subcommands():
    my_sams = [
        sam_random_subcommand,
        sam_handpicked_subcommand,
    ]
    group = "asreviewcontrib.simulation.sam"
    try:
        other_sams = [e.load() for e in entrypoints(group=group)]
    except Exception as e:
        print(get_error_msg(group, e))
        other_sams = []
    for s in sort_commands(my_sams + other_sams):
        cli.add_command(s)


def add_starter_subcommands():
    my_starters = [
        load_settings_subcommand,
    ]
    for s in sort_commands(my_starters):
        cli.add_command(s)


def add_stp_subcommands():
    my_stps = [
        stp_nq_subcommand,
        stp_none_subcommand,
        stp_rel_subcommand,
    ]
    group = "asreviewcontrib.simulation.stp"
    try:
        other_stps = [e.load() for e in entrypoints(group=group)]
    except Exception as e:
        print(get_error_msg(group, e))
        other_stps = []
    for s in sort_commands(my_stps + other_stps):
        cli.add_command(s)


def add_terminator_subcommands():
    my_terminators = [
        start_subcommand,
        print_benchmark_names_subcommand,
        print_settings_subcommand,
        save_settings_subcommand,
    ]
    for t in my_terminators:
        cli.add_command(t)


def get_error_msg(group_name, err):
    return (
        f"Something went wrong loading a module from entrypoint group '{group_name}'. Th"
        + f"e error message was: {err}\nContinuing..."
    )


def sort_commands(commands):
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

Starting a simulation using the default combination of models (sam-random, bal-double, clr-nb, fex-tfidf,
qry-max, stp-rel), each using its default parameterization:

\b
$ {cli_name} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

Instead of a benchmark dataset, you can also supply your own data via the `--in` option, as follows:

$ {cli_name} start --in .{os.sep}myfile.csv --out .{os.sep}project.asreview

$ {cli_name} start --in .{os.sep}myfile.ris --out .{os.sep}project.asreview

$ {cli_name} start --in .{os.sep}myfile.tsv --out .{os.sep}project.asreview

$ {cli_name} start --in .{os.sep}myfile.xlsx --out .{os.sep}project.asreview

Using a different classifier strategy can be accomplished by using one of the 'clr-*' subcommands
before issuing the 'start' subcommand, e.g.:

\b
$ {cli_name} clr-logistic \\
  {' ' * len(cli_name)} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

Subcommands can be chained together, for example using the logistic classifier with
the undersample balancer goes like this:

\b
$ {cli_name} clr-logistic \\
  {' ' * len(cli_name)} bal-undersample \\
  {' ' * len(cli_name)} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

Most subcommands have their own parameterization. Check the help of a subcommand with --help or -h for short, e.g.:

$ {cli_name} clr-logistic --help

Passing parameters to a subcommand goes like this:

\b
$ {cli_name} clr-logistic --class_weight 1.1 \\
  {' ' * len(cli_name)} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

By chaining individually parameterized subcommands, we can compose a variety of configurations, e.g.:

\b
$ {cli_name} sam-random --n_included 10 --n_excluded 15 \\
  {' ' * len(cli_name)} fex-tfidf --ngram_max 2 \\
  {' ' * len(cli_name)} clr-nb --alpha 3.823 \\
  {' ' * len(cli_name)} qry-max-random --fraction_max 0.95 --n_instances 10 \\
  {' ' * len(cli_name)} bal-double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1 \\
  {' ' * len(cli_name)} stp-nq --n_queries 20 \\
  {' ' * len(cli_name)} start --benchmark benchmark:van_de_Schoot_2017 \\
  {' ' * len(cli_name)}       --out .{os.sep}project.asreview

Chained commands are evaluated left to right; make sure to end the chain with
the 'start' command, otherwise it may appear like nothing is happening.

Please report any issues at:

https://github.com/asreview-simulation/asreview-simulation/issues.
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


add_terminator_subcommands()
add_starter_subcommands()
add_sam_subcommands()
add_fex_subcommands()
add_clr_subcommands()
add_qry_subcommands()
add_bal_subcommands()
add_stp_subcommands()
add_ofn_subcommands()
