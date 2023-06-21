import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_cluster_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qry-cluster",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["abbr"] == "cluster"
    params = querier["params"].keys()
    assert len(params) == 3
    assert "n_instances" in params
    assert querier["params"]["n_instances"] == 1
    assert "cluster_size" in params
    assert querier["params"]["cluster_size"] == 350
    assert "update_interval" in params
    assert querier["params"]["update_interval"] == 200
