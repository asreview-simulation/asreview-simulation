import click
from asreview.models.feature_extraction import EmbeddingLSTM
from .._epilog import epilog


name = EmbeddingLSTM.name


@click.command(
    epilog=epilog,
    help="Use Embedding LSTM extractor",
    name=f"fex:{name}",
)
@click.option(
    "--embedding",
    "embedding",
    help="File path of embedding matrix. Required for LSTM models.",
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
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--max_sequence_length",
    "max_sequence_length",
    default=1000,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--n_jobs",
    "n_jobs",
    default=1,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--num_words",
    "num_words",
    default=20000,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--padding",
    "padding",
    default="post",
    help="hyperparameter",
    show_default=True,
    type=click.Choice(["post"]),
)
@click.option(
    "--truncating",
    "truncating",
    default="post",
    help="hyperparameter",
    show_default=True,
    type=click.Choice(["post"]),
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
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.extractor.abbr = name
    obj.extractor.params = {
        "embedding": embedding,
        "loop_sequence": loop_sequence,
        "max_sequence_length": max_sequence_length,
        "n_jobs": n_jobs,
        "num_words": num_words,
        "padding": padding,
        "truncating": truncating,
    }
    obj.provided.extractor = True
