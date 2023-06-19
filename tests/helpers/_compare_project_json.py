import json


def compare_project_json(p1, p2):
    with open(p1 / "project.json", "r") as f:
        expected = json.load(f)
    with open(p2 / "project.json", "r") as f:
        actual = json.load(f)

    assert actual["version"] == expected["version"]
    assert actual["mode"] == expected["mode"]
    assert actual["dataset_path"] == expected["dataset_path"]
    assert actual["feature_matrices"][0]["id"] == expected["feature_matrices"][0]["id"]
    assert (
        actual["feature_matrices"][0]["filename"]
        == expected["feature_matrices"][0]["filename"]
    )
    assert actual["reviews"][0]["status"] == expected["reviews"][0]["status"]
