import json
from click.testing import CliRunner
from asreview_simulation.cli import cli
import pytest


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_undersample
@pytest.mark.stp_min
def test_undersample_balancer_default_parameterization():
    runner = CliRunner()
    args = [
        "bal-undersample",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    balancer = json.loads(result.output)["balancer"]
    assert balancer["abbr"] == "undersample"
    params = balancer["params"].keys()
    assert "ratio" in params
    assert balancer["params"]["ratio"] == 1.0
