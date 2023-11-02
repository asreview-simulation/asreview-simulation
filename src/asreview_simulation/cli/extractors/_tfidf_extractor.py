import click
from asreview.models.feature_extraction import Tfidf
from .._epilog import epilog


name = Tfidf.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use TF-IDF extractor",
    name=f"fex-{name}",
    short_help="TF-IDF extractor",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--ngram_max",
    "ngram_max",
    default=1,
    help="Use n-grams up to ngram_max. For example in the case of ngram_max=2, "
    + "monograms and bigrams could be used.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--split_ta",
    "split_ta",
    help="Include this flag to split ta.",
    is_flag=True,
)
@click.option(
    "--stop_words",
    "stop_words",
    default="english",
    help="When set to 'english', use stopwords. If set to 'none', do not use stop words.",
    show_default=True,
    type=click.Choice(["english", "none"]),
)
@click.option(
    "--use_keywords",
    "use_keywords",
    help="Include this flag to use keywords.",
    is_flag=True,
)
@click.pass_obj
def tfidf_extractor(obj, force, ngram_max, split_ta, stop_words, use_keywords):
    if not force:
        assert obj.provided.extractor is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.extractor.abbr = name
    obj.extractor.params = {
        "ngram_max": ngram_max,
        "split_ta": {False: 0, True: 1}[split_ta],
        "stop_words": stop_words,
        "use_keywords": {False: 0, True: 1}[use_keywords],
    }
    obj.provided.extractor = True
