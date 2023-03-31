from ._base_extractor import BaseExtractor
from ._doc2vec_extractor import Doc2VecExtractor
from ._embedding_idf_extractor import EmbeddingIdfExtractor
from ._embedding_lstm_extractor import EmbeddingLstmExtractor
from ._sbert_extractor import SbertExtractor
from ._tfidf_extractor import TfidfExtractor


del _base_extractor
del _doc2vec_extractor
del _embedding_idf_extractor
del _embedding_lstm_extractor
del _sbert_extractor
del _tfidf_extractor

__all__ = [
    "BaseExtractor",
    "Doc2VecExtractor",
    "EmbeddingIdfExtractor",
    "EmbeddingLstmExtractor",
    "SbertExtractor",
    "TfidfExtractor"
]

for _item in dir():
    if not _item.endswith('__'):
        assert _item in __all__, f"Named export {_item} missing from __all__ in {__package__}"
for _item in __all__:
    assert _item in dir(), f"__all__ includes unknown item {_item} in {__package__}"
del _item
