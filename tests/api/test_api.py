import pytest
import asreviewcontrib.simulation


def get_modules():
    return [
        asreviewcontrib.simulation,
        asreviewcontrib.simulation.api,
        asreviewcontrib.simulation.api.extending,
        asreviewcontrib.simulation.api.plotting,
        asreviewcontrib.simulation.api.unwrapping,
    ]


def get_names(module):
    return {name for name in dir(module) if not name.startswith("__")}


expected = {
    "asreviewcontrib.simulation": {
        "_private",
        "api",
    },
    "asreviewcontrib.simulation.api": {
        "Config",
        "OneModelConfig",
        "draw_sample",
        "extending",
        "get_abbrs",
        "get_dataset_names",
        "get_pyll",
        "plotting",
        "prep_project_directory",
        "run",
        "unwrapping",
    },
    "asreviewcontrib.simulation.api.extending": {
        "dont_reassign_bal_msg",
        "dont_reassign_clr_msg",
        "dont_reassign_fex_msg",
        "dont_reassign_ofn_msg",
        "dont_reassign_qry_msg",
        "dont_reassign_sam_msg",
        "dont_reassign_stp_msg",
        "epilog",
    },
    "asreviewcontrib.simulation.api.plotting": {
        "Padding",
        "TrellisHandles",
        "plot_trellis",
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
