import statsmodels.formula.api as sm


def get_covariates(degree):
    base_variables = [
        "smallm",
        "largem",
        "treatsmall",
        "treatlarge",
        "ssmall",
        "slarge",
        "streatsmall",
        "streatlarge",
    ]
    if degree == 0:
        base = base_variables[0:3]
        return base
    if degree == 1:
        return base_variables
    else:
        for i in range(2, degree + 1):
            base_variables.append(f"ssmall{i}")
            base_variables.append(f"slarge{i}")
            base_variables.append(f"streatsmall{i}")
            base_variables.append(f"streatlarge{i}")
        return base_variables


def regress(independent_Variable, dataframe, degree):
    reg = (
        sm.ols(
            formula=f"{independent_Variable} ~ " + ("+").join(get_covariates(degree)),
            data=dataframe,
        )
        .fit(cov_type="cluster", cov_kwds={"groups": dataframe["score"]}, use_t=True)
        .summary()
    )
    return reg
