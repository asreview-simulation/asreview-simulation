import pytest
from asreview_simulation.api import PartialConfig
from asreview_simulation.api import get_abbrs
from asreview_simulation._private.lib.get_default_params import get_default_params


@pytest.mark.parametrize("abbr", get_abbrs())
def test_construct_partial_config_from_positional_args_abbr_only(abbr):
    actual = PartialConfig(abbr)
    expected = PartialConfig(abbr=abbr, params=get_default_params(abbr))
    assert actual == expected


@pytest.mark.parametrize("abbr", get_abbrs())
def test_construct_partial_config_from_positional_args(abbr):
    actual = PartialConfig(abbr, get_default_params(abbr))
    expected = PartialConfig(abbr=abbr, params=get_default_params(abbr))
    assert actual == expected


@pytest.mark.parametrize("abbr", get_abbrs())
def test_construct_partial_config_from_partial_kwargs(abbr):
    params = get_default_params(abbr)
    if len(params.keys()) >= 1:
        key, _ = list(params.items())[0]
        one_pair = {key: "test value"}
        actual = PartialConfig(abbr=abbr, params=one_pair).params
        expected = params.copy()
        expected.update(one_pair)
        assert actual == expected
    else:
        pytest.skip(reason=f"{abbr} has no parameters to test")


@pytest.mark.parametrize("abbr", get_abbrs())
def test_raising_construct_partial_config_from_kwargs_with_extras(abbr):
    with pytest.raises(AssertionError):
        params = get_default_params(abbr)
        params.update({"xyz123456": "extra key"})
        PartialConfig(abbr=abbr, params=params)


def test_raising_construct_partial_config_nonexistent_model():
    with pytest.raises(KeyError):
        PartialConfig(abbr="xyz")


def test_raising_construct_partial_config_from_positional_args_abbr_only_wrong_type():
    with pytest.raises(AssertionError):
        PartialConfig({"wrong": "type"})


def test_raising_construct_partial_config_from_positional_args_wrong_type():
    with pytest.raises(AssertionError):
        PartialConfig("bal-double", 12345)


