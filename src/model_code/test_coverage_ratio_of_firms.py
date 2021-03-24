import pytest

from src.model_code.coverage_ratio_of_firms import get_covariates


@pytest.fixture
def setup_expected():
    out = {}
    out["degree_0"] = ["treatl", "treath"]
    out["degree_1"] = ["treatl", "treath", "s", "streatl", "streath"]
    out["degree_2"] = [
        "treatl",
        "treath",
        "s",
        "streatl",
        "streath",
        "s2",
        "streatl2",
        "streath2",
    ]
    out["degree_3"] = [
        "treatl",
        "treath",
        "s",
        "streatl",
        "streath",
        "s2",
        "streatl2",
        "streath2",
        "s3",
        "streatl3",
        "streath3",
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
