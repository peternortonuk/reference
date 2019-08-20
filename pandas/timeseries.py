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



import pdb; pdb.set_trace()


date_format = '%d-%b-%Y'  # like this '01-Jan-2018'
date_format_dayname = '%a %d-%m-%Y'
weekmask = 'Mon Tue Wed Thu Fri'
holidays = ['01-Jan-2018', '02-Jan-2018']
holidays = pd.to_datetime(holidays)

date_list = ['01-Jan-2018', '02-Jan-2018', '03-Jan-2018']
start_date_str = '01-Jan-2018'
end_date_str = '01-Feb-2018'
winter_start_date_str = '01-Oct-2016'
clock_change_date = '31-Mar-2019'
long_end_date_str = '01-Jan-2020'

# ==============================================================================
# datetimes

# single Timestamp type
ts = pd.to_datetime(start_date_str, format=date_format)

# range of timestamps as a DateTimeIndex type
dti = pd.date_range(start_date_str, freq='D', periods=3)
# made up of Timestamp objects
dti[0] == ts

# index directly from a list of string dates
dti2 = pd.to_datetime(date_list)
dti == dti2

# or using index constructor
dti3 = pd.DatetimeIndex(date_list)
dti == dti3

# use date_range with start and end dates
dti4 = pd.date_range(start_date_str, end_date_str, freq='D')

# generating business days
dti5 = pd.bdate_range(start_date_str, end_date_str, freq='B')

# requires a custom frequency definition if we define weekmask and we can add holidays
dti6 = dti6 = pd.bdate_range(start_date_str, end_date_str, freq='C', weekmask=weekmask, holidays=holidays)

# show results in df with day name
index = dti6
df = pd.DataFrame(data=index.strftime(date_format_dayname), index=index, columns=['date_as_str'])

# ==============================================================================
# time delta

ts = pd.to_datetime(start_date_str, format=date_format)
ts1 = ts + pd.Timedelta(days=1)

# ==============================================================================
# time spans

# single Period type
p = pd.Period(start_date_str, freq='M')
# which has a start and end time
print(p.start_time, p.end_time)

# range of periods as a PeriodIndex type
pr = pd.period_range(start_date_str, freq='M', periods=3)
# made up of Period objects
p == pr[0]


# ==============================================================================
# DateOffset objects

'''
Timedelta: A Timedelta day will always increment datetimes by 24 hours

DateOffset: While a DateOffset day will increment datetimes to the same time the
next day whether a day represents 23, 24 or 25 hours due to daylight savings time
'''

# compare Timedelta and DateOffset
# to test this need a timestamp object with timezone defined
# cant do this with a to_datetime method
ts = pd.Timestamp(clock_change_date, tz='Europe/Helsinki')
ts1 = ts + pd.Timedelta(days=1)  # returns 1am the following day
ts2 = ts + pd.DateOffset(days=1)  # returns midnight


# add seasons as multiple months
winter_start_date = pd.to_datetime(winter_start_date_str)
# use offsets
one_month = pd.offsets.MonthBegin()
# then multiples
six_months = 6 * one_month
# and add to timestamp
result = winter_start_date + six_months

# or use DateOffset directly
six_months = pd.DateOffset(months=6)

# ==============================================================================
# resample

# generate an index of season dates
dti = pd.date_range(start=winter_start_date, periods=5, freq=six_months)

# convert from DateTimeIndex to PeriodIndex
p = dti.to_period(freq='6M')

# build the dataset required for analysis
start = p.start_time.min()
end = p.end_time.max()
index = pd.date_range(start, end, freq='D')
length = len(index)
df = pd.DataFrame(data=np.random.randn(length), index=index)

# resample; would be nice to use PeriodIndex; but seems to only support string def
x = df.resample('6MS')
print(x.mean())
