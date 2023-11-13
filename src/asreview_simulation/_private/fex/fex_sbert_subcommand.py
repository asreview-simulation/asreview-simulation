import click
from asreview.models.feature_extraction import SBERT
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.fex.fex_sbert_config import get_fex_sbert_config


default_params = get_fex_sbert_config().params
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
        assert obj.provided.fex is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.models.fex.abbr = name
    obj.models.fex.params = {
        "split_ta": split_ta,
        "transformer_model": transformer_model,
        "use_keywords": use_keywords,
    }
    obj.provided.fex = True
