import pytest
import asreview_simulation


def get_modules():
    return [
        asreview_simulation,
        asreview_simulation.api,
        asreview_simulation.api.unwrapping,
    ]


def get_names(module):
    return {name for name in dir(module) if not name.startswith("__")}


expected = {
    "asreview_simulation": {
        "_private",
        "api",
    },
    "asreview_simulation.api": {
        "CompleteConfig",
        "draw_sample",
        "get_abbrs",
        "get_pyll",
        "list_dataset_names",
        "PartialConfig",
        "prep_project_directory",
        "run",
        "unwrapping",
    },
    "asreview_simulation.api.unwrapping": {
        "get_review_simulate_kwargs",
        "instantiate_unwrapped_model",
    },
}


@pytest.mark.parametrize("module", get_modules())
def test_api(module):
    actual = get_names(module)
    assert actual == expected[module.__name__]
