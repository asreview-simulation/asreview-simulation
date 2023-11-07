import click
from asreview.models.feature_extraction import EmbeddingIdf
from asreview_simulation._private.cli_epilog import epilog


name = f"fex-{EmbeddingIdf.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Embedding IDF extractor",
    name=name,
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
@click.option(
    "--split_ta",
    "split_ta",
    help="Include this flag to split ta.",
    is_flag=True,
)
@click.option(
    "--use_keywords",
    "use_keywords",
    help="Include this flag to use keywords.",
    is_flag=True,
)
@click.pass_obj
def fex_embedding_idf_subcommand(obj, embedding, force, split_ta, use_keywords):
    if not force:
        assert obj.provided.extractor is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.models.extractor.abbr = name
    obj.models.extractor.params = {
        "embedding": embedding,
        "split_ta": split_ta,
        "use_keywords": use_keywords,
    }
    obj.provided.extractor = True
