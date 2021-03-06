import json

import pandas as pd

from src.config import BLD
from src.config import SRC


depends_on = SRC / "model_specs" / "baseline" / "degree_0.json"
df = BLD / "data" / "Bronzini-Iachini_dataset.csv"
model = json.loads(depends_on.read_text(encoding="utf-8"))
print(model["n_degree"])


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


inputs = pd.read_csv(df)

print(regress(inputs, 0))
