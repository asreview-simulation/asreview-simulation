import json
import pytest
from click.testing import CliRunner
from asreviewcontrib.simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.clr_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_max_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qry-max",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["qry"]
    assert querier["abbr"] == "qry-max"
    params = querier["params"].keys()
    expected_pairs = [
        ("n_instances", 1),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of querier."
        actual_value = querier["params"][param]
        assert type(actual_value) == type(expected_value), f"Unexpected type for key '{param}'"
        assert actual_value == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
