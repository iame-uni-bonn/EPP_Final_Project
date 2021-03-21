import statsmodels.formula.api as sm


def get_covariates(degree):
    base_variables = ["treatl", "treath", "s", "streatl", "streath"]
    if degree == 0:
        base = base_variables[0:2]
        return base
    if degree == 1:
        return base_variables
    else:
        for i in range(2, degree + 1):
            base_variables.append(f"s{i}")
            base_variables.append(f"streatl{i}")
            base_variables.append(f"streath{i}")

        return base_variables


def regress(dataframe, degree):
    reg = (
        sm.ols(
            formula="INVSALES ~ " + ("+").join(get_covariates(degree)),
            data=dataframe,
        )
        .fit(cov_type="cluster", cov_kwds={"groups": dataframe["score"]}, use_t=True)
        .summary()
    )
    return reg
