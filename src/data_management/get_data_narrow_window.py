# {import pandas as pd
# import pytask
#
# from src.config import BLD
# from src.config import SRC
#
#
# def get_narrow_window(origin, destination):
#     df_full = pd.read_stata(origin)
#     df_narrow = df_full[(df_full.score > 65) & (df_full.score < 75)]
#     file = df_narrow.to_csv(f"{destination}\\" + "Bronzini-Iachini_dataset_narrow_window"
#     + ".csv")
#     return file
#
#
# @pytask.mark.produces(
#        {
#            "Path": SRC / "original_data" / "Bronzini-Iachini_dataset.dta",
#            "Destination": BLD / "data" / "narrow_window",
#    },
# )
# def task_get_narrow_window(produces):
#     get_narrow_window(produces["Path"], produces["Destination"])}
#
#
#  def convert_format(origin, destination):
#     df = pd.read_stata(origin)
