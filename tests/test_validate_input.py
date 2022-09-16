import pytest
from utils.validate_input import validate_type


# Example function
def f(i: int, s: str, l: list, t: tuple, d: dict, se: set):
    i = validate_type(i, int)
    s = validate_type(s, str)
    l = validate_type(l, list)
    t = validate_type(t, tuple)
    d = validate_type(d, dict)
    se = validate_type(se, set)
    return 1


@pytest.fixture
def base_args():
    return [2, "abc", [1, 2, 3], (4, 5, 6), {"a": 1, "b": 2}, {7, 7, 8}]


# Tests
def test_valid_arguments(base_args):
    assert f(*base_args) == 1


def test_convert_argument_of_wrong_type(base_args):
    # string will be converted to integer
    base_args[0] = "2"
    # tuple will be converted to list
    base_args[2] = (1, 2, 3)
    # list will be converted to set
    base_args[-1] = [7, 7, 8]
    assert f(*base_args) == 1


def test_int_argument_of_wrong_type(base_args):
    # string that cannot be converted to integer will cause ValueError
    base_args[0] = "abc"
    with pytest.raises(ValueError):
        f(*base_args)
    # list cannot be conerted to integer, causing TypeError
    base_args[0] = [1]
    with pytest.raises(TypeError):
        f(*base_args)


def test_dict_argument_wrong_type(base_args):
    # integer cannot be converted to dict, causing TypeError
    base_args[4] = 1
    with pytest.raises(TypeError):
        f(*base_args)
