import pytest
from asreviewcontrib.simulation._private.lib.get_default_params import get_default_params
from asreviewcontrib.simulation.api import get_abbrs
from asreviewcontrib.simulation.api import OneModelConfig


@pytest.mark.parametrize("abbr", get_abbrs())
def test_construct_one_model_config_from_positional_args_abbr_only(abbr):
    # constructing from abbr only should yield the default parameter values
    actual = OneModelConfig(abbr)
    expected = OneModelConfig(abbr=abbr, params=get_default_params(abbr))
    assert actual == expected


@pytest.mark.parametrize("abbr", get_abbrs())
def test_construct_one_model_config_from_positional_arg_partial_params(abbr):
    # constructing from abbr and partial params should yield a PartialConfig
    # instance with the default parameter values given the model + changes
    # from the pair passed to the constructor
    params = get_default_params(abbr)
    if len(params.keys()) >= 1:
        key, _ = list(params.items())[0]
        one_pair = {key: "test value"}
        actual = OneModelConfig(abbr, one_pair).params
        expected = params.copy()
        expected.update(one_pair)
        assert actual == expected
    else:
        pytest.skip(reason=f"{abbr} has no parameters to test")


@pytest.mark.parametrize("abbr", get_abbrs())
def test_construct_one_model_config_from_kwargs_partial_params(abbr):
    # constructing from abbr and partial params kwargs should yield a PartialConfig
    # instance with the default parameter values given the model + changes
    # from the pair passed to the constructor
    params = get_default_params(abbr)
    if len(params.keys()) >= 1:
        key, _ = list(params.items())[0]
        one_pair = {key: "test value"}
        actual = OneModelConfig(abbr=abbr, params=one_pair).params
        expected = params.copy()
        expected.update(one_pair)
        assert actual == expected
    else:
        pytest.skip(reason=f"{abbr} has no parameters to test")


def test_raising_construct_one_model_config_nonexistent_model():
    # constructing from an unknown abbr should raise an AsssertionError
    with pytest.raises(KeyError):
        OneModelConfig(abbr="unknown-abbr")


@pytest.mark.parametrize("abbr", get_abbrs())
def test_raising_construct_one_model_config_from_kwargs_with_extras(abbr):
    # constructing from abbr and params using kwargs with an unknown key
    # should raise an AsssertionError
    with pytest.raises(AssertionError):
        params = get_default_params(abbr)
        params.update({"unknown-parameter": "value"})
        OneModelConfig(abbr=abbr, params=params)


def test_raising_construct_one_model_config_from_positional_args_abbr_only_wrong_type():
    # constructing from position argument abbr of the wrong
    # type should raise an AsssertionError
    with pytest.raises(AssertionError):
        OneModelConfig({"wrong": "type"})


def test_raising_construct_one_model_config_from_positional_args_wrong_type():
    # constructing from position argument params of the wrong
    # type should raise an AsssertionError
    with pytest.raises(AssertionError):
        OneModelConfig("bal-double", 12345)
