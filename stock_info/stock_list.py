import tushare as ts
import pandas as pd

pro = ts.pro_api('fb520d160d856e5f849b94dfb8b74fe98a2f6db789b76c0abdf50a8a')

df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
