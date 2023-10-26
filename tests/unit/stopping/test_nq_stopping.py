import json
from click.testing import CliRunner
from asreview_simulation.cli import cli
import pytest


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_nq
def test_nq_stopping_default_parameterization():
    runner = CliRunner()
    args = [
        "stp-nq",
        "--n_queries",
        "25",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    stopping = json.loads(result.output)["stopping"]
    assert stopping["abbr"] == "nq"
    params = stopping["params"].keys()
    assert "n_queries" in params
    assert stopping["params"]["n_queries"] == 25
