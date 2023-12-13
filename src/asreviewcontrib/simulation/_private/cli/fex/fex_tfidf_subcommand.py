import click
from asreview.models.feature_extraction import Tfidf
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_fex_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig
from asreviewcontrib.simulation._private.lib.fex.fex_tfidf_params import get_fex_tfidf_params


default_params = get_fex_tfidf_params()
abbr = f"fex-{Tfidf.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use TF-IDF extractor",
    name=abbr,
    short_help="TF-IDF extractor",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'fex' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--ngram_max",
    "ngram_max",
    default=default_params["ngram_max"],
    help="Use n-grams up to ngram_max. For example in the case of ngram_max=2, monograms and bigrams could be used.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--split_ta",
    "split_ta",
    default=default_params["split_ta"],
    help="Include this flag to split ta.",
    is_flag=True,
)
@click.option(
    "--stop_words",
    "stop_words",
    default=default_params["stop_words"],
    help="When set to 'english', use stopwords. If set to 'none', do not use stop words.",
    show_default=True,
    type=click.Choice(["english", "none"]),
)
@click.option(
    "--use_keywords",
    "use_keywords",
    default=default_params["use_keywords"],
    help="Include this flag to use keywords.",
    is_flag=True,
)
@click.pass_obj
def fex_tfidf_subcommand(obj, force, ngram_max, split_ta, stop_words, use_keywords):
    if not force:
        assert obj.provided.fex is False, dont_reassign_fex_msg
    params = {
        "ngram_max": ngram_max,
        "split_ta": split_ta,
        "stop_words": stop_words,
        "use_keywords": use_keywords,
    }
    obj.config.fex = OneModelConfig(abbr=abbr, params=params)
    obj.provided.fex = True
