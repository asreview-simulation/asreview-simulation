import click
from asreviewlib.extractors import EmbeddingLstmExtractor


name = EmbeddingLstmExtractor.name


@click.command(name=f"e-{name}", help="Use Embedding LSTM extractor")
@click.option("--loop_sequence", "loop_sequence", default=1, type=click.INT, help="hyperparameter 'loop_sequence'.")
@click.option("--num_words", "num_words", default=20000, type=click.INT, help="hyperparameter 'num_words'.")
@click.option("--max_sequence_length", "max_sequence_length", default=1000, type=click.INT,
              help="hyperparameter 'max_sequence_length'.")
@click.option("--padding", "padding", default="post", type=click.STRING, help="hyperparameter 'padding'.")
@click.option("--truncating", "truncating", default="post", type=click.STRING, help="hyperparameter 'truncating'.")
@click.option("--n_jobs", "n_jobs", default=1, type=click.INT, help="hyperparameter 'n_jobs'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the extractor configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def embedding_lstm_extractor(obj, loop_sequence, num_words, max_sequence_length, padding, truncating, n_jobs, force):
    if not force:
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
