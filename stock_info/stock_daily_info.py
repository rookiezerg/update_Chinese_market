import json
import os
import pandas as pd
import tushare as ts
from threading import Thread, Semaphore

path = '/Users/gate/data/'

with open('../config.json') as js:
    api_key = json.load(js)['api_key']

pro = ts.pro_api(api_key)
ts.set_token(api_key)


def stock_list():
    df = pro.stock_basic(exchange='', list_status='L', fields='ts_code')
    stock_list = df['ts_code'].tolist()
    return stock_list


def stock_list_date(ts_code):
    result = pro.stock_basic(ts_code=ts_code, fields='list_date')
    return result.iloc[0, 0]


def stock_info(ts_code, save=False):
    file_path = path+ts_code[:-3]+'.csv'
    if os.path.exists(file_path):
        start_date = pd.read_csv(file_path).trade_date.iloc[-1]
        header_save = False
    else:
        start_date = stock_list_date(ts_code)
        header_save = True

    df = ts.pro_bar(ts_code=ts_code, adj='qfq', start_date=start_date).sort_values(by='trade_date', ascending=True).reset_index(drop=True)

    if save:
        df.to_csv(file_path, mode='a', index=False, header=header_save)
        return
    else:
        return df


def update_stock_daily(sem):
    sem.acquire()
    stocks = stock_list()
    for stock in stocks:
        task = Thread(target=stock_info, args=(stock, True, ))
        task.start()
    return


if __name__ == '__main__':
    sem = Semaphore(10)
    update_stock_daily(sem)
