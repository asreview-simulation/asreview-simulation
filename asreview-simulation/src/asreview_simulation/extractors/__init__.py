from ._doc2vec_extractor import doc2vec_extractor
from ._tfidf_extractor import tfidf_extractor
from ._embedding_idf_extractor import embedding_idf_extractor
from ._embedding_lstm_extractor import embedding_lstm_extractor
from ._sbert_extractor import sbert_extractor


del _doc2vec_extractor
del _tfidf_extractor
del _embedding_idf_extractor
del _embedding_lstm_extractor
del _sbert_extractor


__all__ = [
    "doc2vec_extractor",
    "tfidf_extractor",
    "embedding_idf_extractor",
    "embedding_lstm_extractor",
    "sbert_extractor"
]

for _item in dir():
    if not _item.endswith('__'):
        assert _item in __all__, f"Named export {_item} missing from __all__ in {__package__}"
for _item in __all__:
    assert _item in dir(), f"__all__ includes unknown item {_item} in {__package__}"
del _item
