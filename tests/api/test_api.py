import pytest
import asreviewcontrib


def get_modules():
    return [
        asreviewcontrib,
        asreviewcontrib.simulation,
        asreviewcontrib.simulation.api,
        asreviewcontrib.simulation.api.unwrapping,
    ]


def get_names(module):
    return {name for name in dir(module) if not name.startswith("__")}


expected = {
    "asreviewcontrib": {
        "simulation",
    },
    "asreviewcontrib.simulation": {
        "_private",
        "api",
    },
    "asreviewcontrib.simulation.api": {
        "AllModelConfig",
        "draw_sample",
        "get_abbrs",
        "get_dataset_names",
        "get_pyll",
        "OneModelConfig",
        "prep_project_directory",
        "run",
        "unwrapping",
    },
    "asreviewcontrib.simulation.api.unwrapping": {
        "get_review_simulate_kwargs",
        "instantiate_unwrapped_model",
    },
}


@pytest.mark.parametrize("module", get_modules())
def test_api(module):
    actual = get_names(module)
    assert actual == expected[module.__name__]
