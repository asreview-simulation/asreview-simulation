import json
import pytest
from click.testing import CliRunner
from asreviewcontrib.simulation._private.cli.cli import cli


@pytest.mark.sam_handpicked
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_with_records():
    runner = CliRunner()
    args = [
        "sam-handpicked",
        "--records",
        "1,2,3",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    sampler = json.loads(result.output)["sam"]
    assert sampler["abbr"] == "sam-handpicked"
    params = sampler["params"].keys()
    expected_pairs = [
        ("records", [1, 2, 3]),
        ("rows", None),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of classifier."
        actual_value = sampler["params"][param]
        assert type(actual_value) == type(expected_value), f"Unexpected type for key '{param}'"
        assert actual_value == expected_value, f"Expected key '{param}' to have value '{expected_value}'."


@pytest.mark.sam_handpicked
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_with_rows():
    runner = CliRunner()
    args = [
        "sam-handpicked",
        "--rows",
        "1,2,3",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    sampler = json.loads(result.output)["sam"]
    assert sampler["abbr"] == "sam-handpicked"
    params = sampler["params"].keys()
    expected_pairs = [
        ("records", None),
        ("rows", [1, 2, 3]),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of classifier."
        actual_value = sampler["params"][param]
        assert type(actual_value) == type(expected_value), f"Unexpected type for key '{param}'"
        assert actual_value == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
