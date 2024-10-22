""" The aim is to run a regression of 8 outcome variables on a set of covariates
related to the age of firms. If the coefficient of 'treatfchigh' or 'treatfclow' are
significant, we could conclude that the age of the firm determines the effectiveness
of incentives. The significance of 'treatfchigh'('treatfclow') means that old(young) firms
are affected by the public subsidy.

"""
import econtools.metrics as mt


def get_covariates(degree):
    """Collect the regressors (independent variables).

    Args:
        degree (integer): degree of polynomials

    Returns:
        regressors (list)

    """
    base_variables = [
        "fchighm",
        "fclowm",
        "treatfchigh",
        "treatfclow",
        "sfchigh",
        "sfclow",
        "streatfchigh",
        "streatfclow",
    ]
    if degree == 0:
        base = base_variables[0:4]
        return base
    if degree == 1:
        return base_variables
    else:
        for i in range(2, degree + 1):
            base_variables.append(f"sfchigh{i}")
            base_variables.append(f"sfclow{i}")
            base_variables.append(f"streatfchigh{i}")
            base_variables.append(f"streatfclow{i}")
        return base_variables


def regress(dependent_variable, dataframe, degree):
    """Regress the dependent variables on covariates (independent variables).

    Args:
        dependent_variable (float): the independent variable
        dataframe (pd.DataFrame): the dataframe of full sample, narrow window, and wide window
        degree (integer): degree of polynomials


    Returns:
        regression result(result)


    """

    reg = mt.reg(
        dataframe, f"{dependent_variable}", get_covariates(degree), cluster="score"
    )
    return reg
