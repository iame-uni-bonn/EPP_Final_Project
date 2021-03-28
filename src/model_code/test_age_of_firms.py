import pytest

from src.model_code.age_of_firms import get_covariates


@pytest.fixture
def setup_expected():
    out = {}
    out["degree_0"] = ["fchighm", "fclowm", "treatfchigh", "treatfclow"]
    out["degree_1"] = [
        "fchighm",
        "fclowm",
        "treatfchigh",
        "treatfclow",
        "sfchigh",
        "sfclow",
        "streatfchigh",
        "streatfclow",
    ]
    out["degree_2"] = [
        "fchighm",
        "fclowm",
        "treatfchigh",
        "treatfclow",
        "sfchigh",
        "sfclow",
        "streatfchigh",
        "streatfclow",
        "sfchigh2",
        "sfclow2",
        "streatfchigh2",
        "streatfclow2",
    ]
    out["degree_3"] = [
        "fchighm",
        "fclowm",
        "treatfchigh",
        "treatfclow",
        "sfchigh",
        "sfclow",
        "streatfchigh",
        "streatfclow",
        "sfchigh2",
        "sfclow2",
        "streatfchigh2",
        "streatfclow2",
        "sfchigh3",
        "sfclow3",
        "streatfchigh3",
        "streatfclow3",
    ]
    return out


@pytest.fixture
def degree():
    out = [0, 1, 2, 3]
    return out


def test_get_covariates(setup_expected, degree):
    expected_result = setup_expected
    actual_result = {}
    for i in degree:
        actual_result[f"degree_{i}"] = get_covariates(i)
    assert actual_result == expected_result
