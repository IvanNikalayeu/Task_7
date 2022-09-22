from datetime import timedelta


def min_condition(df):

    for index, row in df.iterrows():
        start_date = row['date'] - timedelta(seconds=60)
        res_df = df.loc[df['date'].between(start_date, row['date'])]
        if len(res_df.index) > 10:
            print(f'from {start_date} till {row["date"]} ALERT More 10 Errors')
