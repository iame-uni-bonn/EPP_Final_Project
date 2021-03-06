import statsmodels.formula.api as sm


def get_covariates(degree):
    base_variables = ["treat", "s", "streat"]
    if degree == 0:
        base = [base_variables[0]]
        return base
    if degree == 1:
        return base_variables
    else:
        for i in range(2, degree + 1):
            base_variables.append(f"s{i}")
            base_variables.append(f"streat{i}")
        return base_variables


def regression(dataframe, degree):
    reg = (
        sm.ols(
            formula="INVSALES ~ " + ("+").join(get_covariates(degree)),
            data=dataframe,
            cov_type="cluster",
        )
        .fit(cov_kwds={"groups": dataframe["score"]}, use_t=True)
        .summary()
    )
    return reg
