import json
import pickle

import pandas as pd
import pytask

from src.config import BLD
from src.config import SRC
from src.model_code.OLS_age import regress


@pytask.mark.parametrize(
    "depends_on, produces",
    [
        (
            {
                "model": SRC
                / "model_specs"
                / "degree_of_polynomials"
                / f"{model_name}.json",
                "OLS_age": SRC / "model_code" / "OLS_age.py",
                "data": BLD / "data" / "Bronzini-Iachini_dataset.csv",
            },
            BLD / "analysis" / "age_of_firm" / f"regression_{model_name}.pickle",
        )
        for model_name in ["degree_0", "degree_1", "degree_2", "degree_3"]
    ],
)
def task_regression(depends_on, produces):
    model = json.loads(depends_on["model"].read_text(encoding="utf-8"))
    inputs = pd.read_csv(depends_on["data"])
    regression = regress(inputs, model["n_degree"])
    with open(produces, "wb") as out_file:
        pickle.dump(regression, out_file)
