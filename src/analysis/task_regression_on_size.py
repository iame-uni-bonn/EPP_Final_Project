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
    model = json.loads(depends_on["model"].read_text(encoding="utf-8"))
    full_sample = pd.read_csv(depends_on["data"])
    wide_window = full_sample[(full_sample.score > 51) & (full_sample.score < 81)]
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
