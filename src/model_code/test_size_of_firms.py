import pytest

from src.model_code.size_of_firms import get_covariates


@pytest.fixture
def setup_expected():
    out = {}
    out["degree_0"] = ["smallm", "largem", "treatsmall", "treatlarge"]
    out["degree_1"] = [
        "smallm",
        "largem",
        "treatsmall",
        "treatlarge",
        "ssmall",
        "slarge",
        "streatsmall",
        "streatlarge",
    ]
    out["degree_2"] = [
        "smallm",
        "largem",
        "treatsmall",
        "treatlarge",
        "ssmall",
        "slarge",
        "streatsmall",
        "streatlarge",
        "ssmall2",
        "slarge2",
        "streatsmall2",
        "streatlarge2",
    ]
    out["degree_3"] = [
        "smallm",
        "largem",
        "treatsmall",
        "treatlarge",
        "ssmall",
        "slarge",
        "streatsmall",
        "streatlarge",
        "ssmall2",
        "slarge2",
        "streatsmall2",
        "streatlarge2",
        "ssmall3",
        "slarge3",
        "streatsmall3",
        "streatlarge3",
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
