import click
from asreview.models.feature_extraction import SBERT
from .._epilog import epilog


name = SBERT.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use SBERT extractor.",
    name=f"fex-{name}",
    short_help="SBERT extractor",
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
    "--transformer_model",
    "transformer_model",
    default="all-mpnet-base-v2",
    help="The transformer model to use. See https://huggingface.co/sentence-transformers for a list of model names.",
    show_default=True,
    type=click.Choice(["all-mpnet-base-v2"]),
)
@click.pass_obj
def sbert_extractor(obj, force, transformer_model):
    if not force:
        assert obj.provided.extractor is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.extractor.abbr = name
    obj.extractor.params = {"transformer_model": transformer_model}
    obj.provided.extractor = True
