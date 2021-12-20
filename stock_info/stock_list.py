import json
import tushare as ts

with open('../config.json') as js:
    api_key = json.load(js)['api_key']

pro = ts.pro_api(api_key)


def stock_list():
    df = pro.stock_basic(exchange='', list_status='L', fields='ts_code')
    ts_code_list = df['ts_code'].tolist()
    return ts_code_list


if __name__ == '__main__':
    print(stock_list())
