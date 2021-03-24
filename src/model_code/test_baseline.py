import pytest

from src.model_code.baseline import get_covariates


@pytest.fixture
def setup_expected():
    out = {}
    out["degree_0"] = ["treat"]
    out["degree_1"] = ["treat", "s", "streat"]
    out["degree_2"] = ["treat", "s", "streat", "s2", "streat2"]
    out["degree_3"] = ["treat", "s", "streat", "s2", "streat2", "s3", "streat3"]
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
