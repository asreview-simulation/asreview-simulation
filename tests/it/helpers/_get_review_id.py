import json


def get_review_id(p):
    with open(p / "project.json", "r") as f:
        project_data = json.load(f)
    return project_data["reviews"][0]["id"]
