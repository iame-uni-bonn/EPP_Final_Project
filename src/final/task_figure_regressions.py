import pickle

import pytask
from fpdf import FPDF

from src.config import BLD


def get_text_result(regression_model):

    model = []
    with open(regression_model, "rb") as pkl:
        try:
            while True:
                model.append(pickle.load(pkl))
        except EOFError:
            pass
    text_file = open("Output.txt", "w+")
    for result in model:
        text_file.write(result.as_text())
    return text_file.close()


@pytask.mark.parametrize(
    "depends_on, produces",
    [
        (
            BLD / "analysis" / "baseline" / f"regression_{model_name}.pickle",
            BLD / "figures" / "baseline" / f"regression_{model_name}.pdf",
        )
        for model_name in ["degree_0", "degree_1", "degree_2", "degree_3"]
    ],
)
def task_figure_regressions(depends_on, produces):
    get_text_result(depends_on)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    # open the text file in read mode
    f = open("output.txt")
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align="C")

    pdf.output(produces)
