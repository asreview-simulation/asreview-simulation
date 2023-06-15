import click
from asreview.models.feature_extraction import Tfidf
from .._epilog import epilog


name = Tfidf.name


@click.command(
    epilog=epilog,
    help="Use TF-IDF extractor",
    name=f"fex:{name}",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--ngram_max",
    "ngram_max",
    default=1,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--stop_words",
    "stop_words",
    default="english",
    help="hyperparameter",
    show_default=True,
    type=click.Choice(["english", "none"]),
)
@click.pass_obj
def tfidf_extractor(obj, force, ngram_max, stop_words):
    if not force:
        assert obj.provided.extractor is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.extractor.abbr = name
    obj.extractor.params = {"ngram_max": ngram_max, "stop_words": stop_words}
    obj.provided.extractor = True
