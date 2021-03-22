import econtools.metrics as mt


def get_covariates(degree):
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
    reg = mt.reg(
        dataframe, f"{dependent_variable}", get_covariates(degree), cluster="score"
    )
    return reg
