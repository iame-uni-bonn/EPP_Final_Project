import statsmodels.formula.api as sm


def get_covariates(degree):
    """Collect the regressors (independent variables).

    Args:
        degree (integer): degree of polynomials

    Returns:
        regressors (list)

    """

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
        base = base_variables[0:4]
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
    """Regress the dependent variables on covariates (independent variables).

    Args:
        dependent_variable (float): the independent variable
        dataframe (pd.DataFrame): the dataframe of full sample, narrow window, and wide window
        degree (integer): degree of polynomials


    Returns:
        regression result(summary)


    """

    reg = (
        sm.ols(
            formula=f"{independent_Variable} ~ " + ("+").join(get_covariates(degree)),
            data=dataframe,
        )
        .fit(cov_type="cluster", cov_kwds={"groups": dataframe["score"]}, use_t=True)
        .summary()
    )
    return reg
