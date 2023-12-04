import json
import pytest
from click.testing import CliRunner
from asreviewcontrib.simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_undersample
@pytest.mark.stp_rel
def test_undersample_balancer_default_parameterization():
    runner = CliRunner()
    args = [
        "bal-undersample",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    balancer = json.loads(result.output)["bal"]
    assert balancer["abbr"] == "bal-undersample"
    params = balancer["params"].keys()
    expected_pairs = [
        ("ratio", 1.0),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of balancer."
        actual_value = balancer["params"][param]
        assert type(actual_value) == type(expected_value), f"Unexpected type for key '{param}'"
        assert actual_value == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
