"""  The aim is to regress the outcome variables on size related covariates.
There are three different samples: 1) full sample: 357 firms, 2) wide_window: 171 firms
with scores between (51,81) and 3) narrow_window: 115 firms with scores between (65,79).
The significance of 'treatsmall' or 'treatlarge' shows that the funding program was effective
regarding the size of frims.

The result of our replication can be compered to the Table 5_Effect of the Program on
Investment by Firm Size of the paper.

"""
import json
import pickle

import pandas as pd
import pytask

from src.config import BLD
from src.config import SRC
from src.model_code.size_of_firms import regress


@pytask.mark.parametrize(
    "depends_on, produces",
    [
        (
            {
                "model": SRC
                / "model_specs"
                / "degree_of_polynomials"
                / f"{model_name}.json",
                "regression": SRC / "model_code" / "size_of_firms.py",
                "data": BLD / "data" / "Bronzini-Iachini_dataset.csv",
            },
            BLD / "analysis" / "size_small_large" / f"regression_{model_name}.pickle",
        )
        for model_name in ["degree_0", "degree_1", "degree_2", "degree_3"]
    ],
)
def task_regression(depends_on, produces):
    # Read models saved in json files
    model = json.loads(depends_on["model"].read_text(encoding="utf-8"))
    # full sample uses the all 357 firms
    full_sample = pd.read_csv(depends_on["data"])
    # Wide window uses the all 171 firms scores of which are between (51,81)
    wide_window = full_sample[(full_sample.score > 51) & (full_sample.score < 81)]
    #  narrow window uses the all 115 firms scores of which are between(65,79),which
    #  is the closest version to a randomized experiment
    narrow_window = full_sample[(full_sample.score > 65) & (full_sample.score < 79)]
    sample = [full_sample, wide_window, narrow_window]
    dependent_variable = [
        "INVSALES",
        "INVTSALES",
        "INVINTSALES",
        "INVK",
        "INVA",
        "LCSALES",
        "SCSALES",
    ]
    with open(produces, "wb") as out_file:
        for df in sample:
            for dv in dependent_variable:
                regression = regress(dv, df, model["n_degree"])
                pickle.dump(regression, out_file)
