import click
from asreview.models.feature_extraction import EmbeddingIdf
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_fex_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig
from asreviewcontrib.simulation._private.lib.fex.fex_embedding_idf_params import get_fex_embedding_idf_params


default_params = get_fex_embedding_idf_params()
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
    help="Force setting the 'fex' configuration, even if that means overwriting a previous configuration.",
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
        assert obj.provided.fex is False, dont_reassign_fex_msg
    params = {
        "embedding": embedding,
        "split_ta": split_ta,
        "use_keywords": use_keywords,
    }
    obj.config.fex = OneModelConfig(abbr=name, params=params)
    obj.provided.fex = True
