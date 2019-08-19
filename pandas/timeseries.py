'''
reference
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases

string formats
http://strftime.org/

'''

import datetime
import pprint as pp
import pandas as pd
import numpy as np
from data import df_long_dates




x = df_long_dates.resample('5min')
print(x.mean())


start = datetime.datetime(2011, 1, 1)
end = datetime.datetime(2012, 1, 1)

# business days
weekmask = 'Mon Tue Wed Thu Fri'
holidays = [datetime.datetime(2011, 1, 5), datetime.datetime(2011, 3, 14)]
dateindex = pd.bdate_range(start, end, freq='C', weekmask=weekmask, holidays=holidays)

# show results with day name
date_format_str = '%a %d-%m-%Y'
df = pd.DataFrame(data=dateindex.strftime(date_format_str), index=dateindex, columns=['date_as_str'])

