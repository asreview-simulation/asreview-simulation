from ._calc_hash import calc_hash
from ._get_review_id import get_review_id


def compare_settings_metadata_json(p1, p2):
    settings1 = p1 / "reviews" / get_review_id(p1) / "settings_metadata.json"
    settings2 = p2 / "reviews" / get_review_id(p2) / "settings_metadata.json"
    assert calc_hash(settings1) == calc_hash(settings2)
