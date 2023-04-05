from .extractors import Doc2VecExtractor
from .extractors import EmbeddingIdfExtractor
from .extractors import EmbeddingLstmExtractor
from .extractors import SbertExtractor
from .extractors import TfidfExtractor
from importlib.metadata import entry_points as entrypoints


def list_extractors():
    my_extractors = {e.name: e for e in [
        Doc2VecExtractor,
        EmbeddingIdfExtractor,
        EmbeddingLstmExtractor,
        SbertExtractor,
        TfidfExtractor
    ]}
    try:
        other_extractors = {e.name: e.load() for e in entrypoints(group="asreviewlib.extractors")}
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreviewlib.extractors'. The error message was: {e}\nContinuing...")
        other_extractors = {}
    d = dict()
    d.update(my_extractors)
    d.update(other_extractors)
    return dict(sorted(d.items()))
