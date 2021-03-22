# import pandas as pd
# import pytask
#
# from src.config import BLD
# from src.config import SRC
#
#
# def get_wide_window(origin, destination):
#     df_full = pd.read_stata(origin)
#     df_wide= df_full[(df_full.score>51)&(df_full.score<81)]
#     csv = df_wide.to_csv(f"{destination}\\" + "Bronzini-Iachini_dataset_wide_window" + ".csv")
#     return csv
#
#
# @pytask.mark.produces(
#        {
#            "Path": SRC / "original_data" / "Bronzini-Iachini_dataset.dta",
#            "Destination": BLD / "data" / "wide_window",
#    },
# )
# def task_get_wide_window(produces):
#     get_wide_window(produces["Path"], produces["Destination"])
#
#
# # def convert_format(origin, destination):
# #     df = pd.read_stata(origin)
# #     csv_file = df.to_csv(destination+"\\" + "Bronzini-Iachini_dataset" + ".csv")
# #     return csv_file
# #
# # @pytask.mark.parametrize(
# #     "depends_on, produces",
# #     (
# #             SRC / "original_data" / "Bronzini-Iachini_dataset.dta",
# #             BLD / "data",
# #     ),
# # )
# #
# # def task_convert_format(depends_on, produces):
# #     convert_format(depends_on, produces)
