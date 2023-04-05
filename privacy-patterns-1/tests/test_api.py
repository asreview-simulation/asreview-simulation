import privacy_patterns_1
import inspect
import pytest


def list_members(pkg):
    r = list()
    members = inspect.getmembers(pkg)
    for name, value in members:
        if name.endswith('__'):
            continue
        r.append(f"{pkg.__name__}.{name}")
        if inspect.ismodule(value):
            r += list_members(value)
    return r


actual_members = list_members(privacy_patterns_1)
expected_members = [
    "privacy_patterns_1.demo",
    "privacy_patterns_1.demo.fun"
]


@pytest.mark.parametrize("expected_member", expected_members)
def test_api_expected_members_present(expected_member):
    assert expected_member in actual_members, f"Didn't find expected member {expected_member} in the API."


@pytest.mark.parametrize("actual_member", actual_members)
def test_api_no_unintentional_exports(actual_member):
    assert actual_member in expected_members, f"Found unexpected member {actual_member} in the API."
