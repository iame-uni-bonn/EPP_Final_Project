import statsmodels.formula.api as sm


def get_covariates(degree):
    """Collect the regressors (independent variables).

    Args:
        degree (integer): degree of polynomials

    Returns:
        regressors (list)

    """

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


def regress(dependent_variable, dataframe, degree):
    """Regress the dependent variables on covariates (independent variables).

    Args:
        dependent_variable (float): the independent variable
        dataframe (pd.DataFrame): the dataframe of full sample, narrow window, and wide window
        degree (integer): degree of polynomials


    Returns:
        regression result(text)


    """

    reg = (
        sm.ols(
            formula=f"{dependent_variable} ~ " + ("+").join(get_covariates(degree)),
            data=dataframe,
        )
        .fit(cov_type="cluster", cov_kwds={"groups": dataframe["score"]}, use_t=True)
        .summary()
    )
    return reg