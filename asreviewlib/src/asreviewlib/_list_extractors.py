from .extractors import Doc2VecExtractor
from .extractors import EmbeddingIdfExtractor
from .extractors import EmbeddingLstmExtractor
from .extractors import SbertExtractor
from .extractors import TfidfExtractor


def list_extractors():
    extractors = [
        Doc2VecExtractor,
        EmbeddingIdfExtractor,
        EmbeddingLstmExtractor,
        SbertExtractor,
        TfidfExtractor
    ]
    return {e.name: e for e in extractors}
