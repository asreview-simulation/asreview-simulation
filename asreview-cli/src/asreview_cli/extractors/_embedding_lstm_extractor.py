import click
from asreviewlib.extractors import EmbeddingLstmExtractor


name = EmbeddingLstmExtractor.name


@click.command(name=f"e-{name}", help="Use Embedding LSTM extractor")
@click.option("-loop_sequence", "loop_sequence", default=1, type=int, help="hyperparameter 'loop_sequence'.")
@click.option("-num_words", "num_words", default=20000, type=int, help="hyperparameter 'num_words'.")
@click.option("-max_sequence_length", "max_sequence_length", default=1000, type=int,
              help="hyperparameter 'max_sequence_length'.")
@click.option("-padding", "padding", default="post", type=str, help="hyperparameter 'padding'.")
@click.option("-truncating", "truncating", default="post", type=str, help="hyperparameter 'truncating'.")
@click.option("-n_jobs", "n_jobs", default=1, type=int, help="hyperparameter 'n_jobs'.")
@click.pass_obj
def embedding_lstm_extractor(obj, loop_sequence, num_words, max_sequence_length, padding, truncating, n_jobs):
    assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {
        "loop_sequence": loop_sequence,
        "num_words": num_words,
        "max_sequence_length": max_sequence_length,
        "padding": padding,
        "truncating": truncating,
        "n_jobs": n_jobs
    }
    obj.provided.extractor = True
