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
    other_extractors = {e.name: e.load() for e in entrypoints(group="asreviewlib.extractors")}
    rv = dict()
    rv.update(my_extractors)
    rv.update(other_extractors)
    return rv
