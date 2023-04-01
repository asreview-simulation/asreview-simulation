from ._double import double
from ._simple import simple
from ._triple import triple
from ._undersample import undersample


del _double
del _simple
del _triple
del _undersample

__all__ = [
    "double",
    "simple",
    "triple",
    "undersample"
]

for _item in dir():
    if not _item.endswith('__'):
        assert _item in __all__, f"Named export {_item} missing from __all__ in {__package__}"
for _item in __all__:
    assert _item in dir(), f"__all__ includes unknown item {_item} in {__package__}"
del _item
