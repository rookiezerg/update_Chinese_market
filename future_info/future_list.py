import json
import tushare as ts

with open('../config.json') as js:
    api_key = json.load(js)['api_key']

pro = ts.pro_api(api_key)


