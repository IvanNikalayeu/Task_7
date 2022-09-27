from datetime import timedelta
import numpy as np


# def min_condition(df):
#
#     for index, row in df.iterrows():
#         start_date = row['date'] - timedelta(seconds=60)
#         res_df = df.loc[df['date'].between(start_date, row['date'])]
#         if len(res_df.index) > 10:
#             print(f'from {start_date} till {row["date"]} ALERT More 10 Errors')

# При применении NumPy скорость обработки увеличивается на 32% при кол-ве 30000 строк
def min_condition(df):

    for index, row in df.iterrows():
        start_date = row['date'] - timedelta(seconds=60)
        idx = np.where((df['date']>start_date) & (df['date']<=row['date']))

        if len(idx[0]) > 10:
            print(f'from {start_date} till {row["date"]} ALERT More 10 Errors')

