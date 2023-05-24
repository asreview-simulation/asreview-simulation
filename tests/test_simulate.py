import os
from tempfile import TemporaryDirectory
from asreview.entry_points import SimulateEntryPoint


def test_simulate_start():

    with TemporaryDirectory(prefix="pytest.") as d:
        args = [
            "benchmark:van_de_Schoot_2017",
            "--state_file", os.path.join(d, "simulate.asreview"),
            "--model", "nb",
            "--query_strategy", "max",
            "--balance_strategy", "double",
            "--feature_extraction", "tfidf"
        ]
        SimulateEntryPoint().execute(args)

    assert True
