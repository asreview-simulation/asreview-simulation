import click
from asreview.models.feature_extraction import EmbeddingIdf
from .._epilog import epilog


name = EmbeddingIdf.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Embedding IDF extractor",
    name=f"fex-{name}",
    short_help="Embedding IDF extractor",
)
@click.option(
    "--embedding",
    "embedding",
    help="File path of embedding matrix.",
    type=click.Path(exists=True),
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def embedding_idf_extractor(obj, embedding, force):
    if not force:
        assert obj.provided.extractor is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.extractor.abbr = name
    obj.extractor.params = {
        "embedding_fp": embedding or "",
    }
    obj.provided.extractor = True
