"""Read, convert, and transfer the original data to the path ROOT / "bld".

"""
import pandas as pd
import pytask

from src.config import BLD
from src.config import SRC


def convert_format(origin, destination):
    """Convert the format of dataset from .dta to .csv.

    Args:

    origin(system path): the path of which original data comes.
    destination(system path): the path to which the converted data to save.

    Returns:
        csv file of dataset

    """
    df = pd.read_stata(origin)
    csv_file = df.to_csv(
        f"{destination}\\" + "Bronzini-Iachini_dataset_full_sample" + ".csv"
    )
    return csv_file


@pytask.mark.produces(
    {
        "Path": SRC / "original_data" / "Bronzini-Iachini_dataset.dta",
        "Destination": BLD / "data",
    },
)
def task_convert_format(produces):
    convert_format(produces["Path"], produces["Destination"])


# def convert_format(origin, destination):
#     df = pd.read_stata(origin)
#     csv_file = df.to_csv(destination+"\\" + "Bronzini-Iachini_dataset" + ".csv")
#     return csv_file
#
# @pytask.mark.parametrize(
#     "depends_on, produces",
#     (
#             SRC / "original_data" / "Bronzini-Iachini_dataset.dta",
#             BLD / "data",
#     ),
# )
#
# def task_convert_format(depends_on, produces):
#     convert_format(depends_on, produces)
