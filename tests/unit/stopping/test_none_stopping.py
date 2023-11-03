import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_none
def test_none_stopping_default_parameterization():
    runner = CliRunner()
    args = [
        "stp-none",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    stopping = json.loads(result.output)["stopping"]
    assert stopping["abbr"] == "none"
    params = stopping["params"].keys()
    assert len(params) == 0
