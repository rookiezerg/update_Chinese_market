import tushare as ts
import pandas as pd

pro = ts.pro_api()

df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
