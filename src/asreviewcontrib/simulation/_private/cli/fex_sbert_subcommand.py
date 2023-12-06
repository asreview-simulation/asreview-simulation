import click
from asreview.models.feature_extraction import SBERT
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_fex_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig
from asreviewcontrib.simulation._private.lib.fex.fex_sbert_params import get_fex_sbert_params


default_params = get_fex_sbert_params()
name = f"fex-{SBERT.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use SBERT extractor.",
    name=name,
    short_help="SBERT extractor",
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
    "--transformer_model",
    "transformer_model",
    default=default_params["transformer_model"],
    help="The transformer model to use. See https://huggingface.co/sentence-transformers for a list of model names.",
    show_default=True,
    type=click.Choice(["all-mpnet-base-v2"]),
)
@click.option(
    "--use_keywords",
    "use_keywords",
    default=default_params["use_keywords"],
    help="Include this flag to use keywords.",
    is_flag=True,
)
@click.pass_obj
def fex_sbert_subcommand(obj, force, split_ta, transformer_model, use_keywords):
    if not force:
        assert obj.provided.fex is False, dont_reassign_fex_msg
    params = {
        "split_ta": split_ta,
        "transformer_model": transformer_model,
        "use_keywords": use_keywords,
    }
    obj.config.fex = OneModelConfig(abbr=name, params=params)
    obj.provided.fex = True
