import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_double_balancer_default_parameterization():
    runner = CliRunner()
    args = [
        "bal-double",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    balancer = json.loads(result.output)["balancer"]
    assert balancer["abbr"] == "double"
    params = balancer["params"].keys()
    expected_pairs = [
        ("a", 2.155),
        ("alpha", 0.94),
        ("b", 0.789),
        ("beta", 1.0),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of balancer."
        assert balancer["params"][param] == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
