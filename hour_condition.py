from datetime import timedelta


def hour_condition(df):
    _df = df
    _num_rows = len(_df.index)
    _time_period = timedelta(seconds=3600)
    for i in range(_num_rows):
        _end_date = _df.iloc[i]['date']
        _start_date = _end_date-_time_period
        _df_res = _df\
            .loc[(_df['date'] > _start_date) & (_df['date'] <= _end_date)]\
            .groupby('bundle_id', as_index=False)\
            .agg({'error_code' : 'count'})\
            .rename(columns={'error_code':'number_of_errors'})\
            .sort_values('number_of_errors', ascending=False)
        if _df_res.number_of_errors.max()>10:
            _res = _df_res.query('number_of_errors > 10')
            print(f'{_start_date} till {_end_date} more 10 Errors in 1 hour \n {_res} \n ', '_'*60)
