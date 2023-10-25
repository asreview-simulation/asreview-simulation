import click
from asreview.models.feature_extraction import EmbeddingLSTM
from .._epilog import epilog


name = EmbeddingLSTM.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Embedding LSTM extractor",
    name=f"fex-{name}",
    short_help="Embedding LSTM extractor",
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
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--loop_sequence",
    "loop_sequence",
    default=1,
    help="Instead of zeros at the start/end of sequence loop it.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--max_sequence_length",
    "max_sequence_length",
    default=1000,
    help="Maximum length of the sequence. Shorter gets truncated. Longer sequences get either "
    + "padded with zeros or looped.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_jobs",
    "n_jobs",
    default=1,
    help="Number of processors used in reading the embedding matrix.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--num_words",
    "num_words",
    default=20000,
    help="Maximum number of unique words to be processed.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--padding",
    "padding",
    default="post",
    help="Which side should be padded.",
    show_default=True,
    type=click.Choice(["pre", "post"]),
)
@click.option(
    "--truncating",
    "truncating",
    default="post",
    help="Which side should be truncated.",
    show_default=True,
    type=click.Choice(["pre", "post"]),
)
@click.pass_obj
def embedding_lstm_extractor(
    obj,
    embedding,
    force,
    loop_sequence,
    max_sequence_length,
    n_jobs,
    num_words,
    padding,
    truncating,
):
    if not force:
        assert obj.provided.extractor is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.extractor.abbr = name
    obj.extractor.params = {
        "embedding_fp": embedding,
        "loop_sequence": loop_sequence,
        "max_sequence_length": max_sequence_length,
        "n_jobs": n_jobs,
        "num_words": num_words,
        "padding": padding,
        "truncating": truncating,
    }
    obj.provided.extractor = True
