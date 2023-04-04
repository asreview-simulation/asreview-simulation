import click

from .balancers import double_balancer
from .balancers import no_balancer
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
from ._load_config import load_config
from ._print_settings import print_settings
from ._start import start
from ._state import State


def cli_help(cli_name="asreview-cli"):
    return f"""
Example usage:

  $ {cli_name} print-settings

  $ {cli_name} start labeled-records.db

Commands can be chained together, e.g.


  $ {cli_name} load-config thefile.cfg start labeled-records.db

  $ {cli_name} b-double --alpha 1.23 print-settings --pretty

  $ {cli_name} b-none c-nb e-tfidf q-mixed start labeled-records.db

\b
  $ {cli_name} s-random --n_included 10 --n_excluded 15                      \\
    {' ' * len(cli_name)} e-tfidf --ngram_max 2                                         \\
    {' ' * len(cli_name)} c-nb --alpha 3.823                                            \\
    {' ' * len(cli_name)} q-mixed --strategy1 max --strategy2 random --mix_ratio 0.95   \\
    {' ' * len(cli_name)} b-double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1           \\
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


cli.add_command(double_balancer)
cli.add_command(no_balancer)
cli.add_command(triple_balancer)
cli.add_command(undersample_balancer)
cli.add_command(naive_bayes_classifier)
cli.add_command(random_forest_classifier)
cli.add_command(logistic_classifier)
cli.add_command(lstm_base_classifier)
cli.add_command(lstm_pool_classifier)
cli.add_command(nn_2_layer_classifier)
cli.add_command(svm_classifier)
cli.add_command(doc2vec_extractor)
cli.add_command(tfidf_extractor)
cli.add_command(embedding_idf_extractor)
cli.add_command(embedding_lstm_extractor)
cli.add_command(sbert_extractor)
cli.add_command(random_prior_sampler)
cli.add_command(handpicked_prior_sampler)
cli.add_command(cluster_querier)
cli.add_command(mixed_querier)
cli.add_command(load_config)
cli.add_command(print_settings)
cli.add_command(start)
