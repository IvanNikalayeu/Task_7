import pandas as pd


def read():

    _names = ['error_code', 'error_message', 'severity', 'log_location', 'mode', 'model', 'graphics', 'session_id',
              'sdkv', 'test_mode', 'flow_id', 'flow_type', 'sdk_date', 'publisher_id', 'game_id', 'bundle_id', 'appv',
              'language', 'os', 'adv_id', 'gdpr', 'ccpa', 'country_code', 'date']

    _df = pd.read_csv('data.csv', header=0, names=_names, nrows=10000)
    _df = _df.query("severity=='Error'")
    _df = _df[['error_code','bundle_id', 'date']]
    _df['date'] = pd.to_datetime(_df['date'], unit='s')
    df = _df.sort_values(by='date').reset_index(drop=True)

    return df

