import click
from asreview.models.feature_extraction import EmbeddingIdf
from asreview_simulation._private.cli_epilog import epilog
from asreview_simulation._private.fex.fex_embedding_idf_config import get_fex_embedding_idf_config


default_params = get_fex_embedding_idf_config().params
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
    default=default_params["embedding"],
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
    default=default_params["split_ta"],
    help="Include this flag to split ta.",
    is_flag=True,
)
@click.option(
    "--use_keywords",
    "use_keywords",
    default=default_params["use_keywords"],
    help="Include this flag to use keywords.",
    is_flag=True,
)
@click.pass_obj
def fex_embedding_idf_subcommand(obj, embedding, force, split_ta, use_keywords):
    if not force:
        assert obj.provided.fex is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.models.fex.abbr = name
    obj.models.fex.params = {
        "embedding": embedding,
        "split_ta": split_ta,
        "use_keywords": use_keywords,
    }
    obj.provided.fex = True
