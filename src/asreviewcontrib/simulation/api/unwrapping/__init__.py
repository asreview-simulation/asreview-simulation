"""
Offers functionality to unwrap the abstraction layer provided by
`asreviewcontrib.simulation`, in order to get objects from the
`asreview` library directly.

Example usage:

    ```python
    from asreviewcontrib.simulation.api.unwrapping import get_review_simulate_kwargs


    # (do something interesting with get_review_simulate_kwargs)
    ```
"""
from asreviewcontrib.simulation._private.lib.unwrapping.get_review_simulate_kwargs import get_review_simulate_kwargs
from asreviewcontrib.simulation._private.lib.unwrapping.instantiate_unwrapped_model import instantiate_unwrapped_model


__all__ = [
    "get_review_simulate_kwargs",
    "instantiate_unwrapped_model",
]
