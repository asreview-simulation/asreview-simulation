import click
from asreviewlib.extractors import EmbeddingLstmExtractor
from .._epilog import epilog


name = EmbeddingLstmExtractor.name


@click.command(epilog=epilog,
               help="Use Embedding LSTM extractor",
               name=f"e-{name}")
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--loop_sequence", "loop_sequence",
              default=1,
              help="hyperparameter 'loop_sequence'.",
              show_default=True,
              type=click.INT)
@click.option("--max_sequence_length", "max_sequence_length",
              default=1000,
              help="hyperparameter 'max_sequence_length'.",
              show_default=True,
              type=click.INT)
@click.option("--n_jobs", "n_jobs",
              default=1,
              help="hyperparameter 'n_jobs'.",
              show_default=True,
              type=click.INT)
@click.option("--num_words", "num_words",
              default=20000,
              help="hyperparameter 'num_words'.",
              show_default=True,
              type=click.INT)
@click.option("--padding", "padding",
              default="post",
              help="hyperparameter 'padding'.",
              show_default=True,
              type=click.Choice(["post"]))
@click.option("--truncating", "truncating",
              default="post",
              help="hyperparameter 'truncating'.",
              show_default=True,
              type=click.Choice(["post"]))
@click.pass_obj
def embedding_lstm_extractor(obj, force, loop_sequence, max_sequence_length, n_jobs, num_words, padding, truncating):
    if not force:
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {
        "loop_sequence": loop_sequence,
        "max_sequence_length": max_sequence_length,
        "n_jobs": n_jobs,
        "num_words": num_words,
        "padding": padding,
        "truncating": truncating
    }
    obj.provided.extractor = True
