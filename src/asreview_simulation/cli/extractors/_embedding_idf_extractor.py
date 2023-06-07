import click
from asreview.models.feature_extraction import EmbeddingIdf
from .._epilog import epilog


name = EmbeddingIdf.name


@click.command(
    epilog=epilog,
    help="Use Embedding IDF extractor",
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
@click.pass_obj
def embedding_idf_extractor(obj, force):
    if not force:
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.extractor.abbr = name
    obj.extractor.params = {}
    obj.provided.extractor = True
