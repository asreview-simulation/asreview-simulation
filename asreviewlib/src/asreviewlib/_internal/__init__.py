from ._check_star_exports import check_star_exports


del _check_star_exports

__all__ = [
    "check_star_exports"
]

check_star_exports(__package__, dir(), __all__)
