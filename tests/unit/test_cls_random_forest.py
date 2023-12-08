import json
import pytest
from click.testing import CliRunner
from asreviewcontrib.simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.clr_rf
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_random_forest_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "clr-rf",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["clr"]
    assert classifier["abbr"] == "clr-rf"
    params = classifier["params"].keys()
    expected_pairs = [
        ("class_weight", 1.0),
        ("max_features", 10),
        ("n_estimators", 100),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of classifier."
        actual_value = classifier["params"][param]
        assert type(actual_value) == type(expected_value), f"Unexpected type for key '{param}'"
        assert actual_value == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
