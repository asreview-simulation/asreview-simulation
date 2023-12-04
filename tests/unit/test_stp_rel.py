import json
import pytest
from click.testing import CliRunner
from asreviewcontrib.simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_min_stopping_default_parameterization():
    runner = CliRunner()
    args = [
        "stp-rel",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    stopping = json.loads(result.output)["stp"]
    assert stopping["abbr"] == "stp-rel"
    params = stopping["params"].keys()
    assert len(params) == 0
