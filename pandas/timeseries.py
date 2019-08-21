'''
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html

    Tables of args:
    (1) Date offsets and associated frequency strings:
        https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
    (2) Offset aliases:
        https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
    (3) Anchored offsets:
        https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#anchored-offsets

    String formats
    http://strftime.org/
'''

import pprint as pp
import pandas as pd
import numpy as np

date_format = '%d-%b-%Y'  # like this '01-Jan-2018'
date_format_dayname = '%a %d-%m-%Y'
weekmask = 'Mon Tue Wed Thu Fri'
holidays = ['01-Jan-2018', '02-Jan-2018']
holidays = pd.to_datetime(holidays)

date_list = ['01-Jan-2018', '02-Jan-2018', '03-Jan-2018']

start_date_str = '01-Jan-2018'
end_date_str = '01-Feb-2018'

winter_start_date_str = '01-Oct-2016'
long_end_date_str = '01-Apr-2020'

clock_change_date = '31-Mar-2019'

# ==============================================================================
'''
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#converting-to-timestamps
Converting to timestamps
    To convert a Series or list-like object of date-like objects e.g. strings, 
    epochs, or a mixture, you can use the to_datetime function
'''

# single Timestamp type; providing a format argument
ts = pd.to_datetime(start_date_str, format=date_format)

# generates a DatetimeIndex
dti = pd.to_datetime(date_list)

# index directly from a list of string dates
dti = pd.DatetimeIndex(date_list)

# ==============================================================================
'''
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#generating-ranges-of-timestamps
Generating ranges of timestamps
    Convenience functions like date_range and bdate_range can utilize a variety of frequency aliases
'''

# range of timestamps as a DateTimeIndex type
dti = pd.date_range(start_date_str, freq='D', periods=3)
# made up of Timestamp objects

# use date_range with start and end dates
dti = pd.date_range(start_date_str, end_date_str, freq='D')

# generating business days
dti = pd.bdate_range(start_date_str, end_date_str, freq='B')

# requires a custom frequency definition if we define weekmask and we can add holidays
dti = pd.bdate_range(start_date_str, end_date_str, freq='C', weekmask=weekmask, holidays=holidays)

# show results in df with day name
df = pd.DataFrame(data=dti.strftime(date_format_dayname), index=dti, columns=['date_as_str'])


# ==============================================================================
'''
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
DateOffset objects:
   Timedelta: A Timedelta day will always increment datetimes by 24 hours
   DateOffset: While a DateOffset day will increment datetimes to the same time the
      next day whether a day represents 23, 24 or 25 hours due to daylight savings time
'''

# time delta
ts = pd.to_datetime(start_date_str, format=date_format)
ts1 = ts + pd.Timedelta(days=1)

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
'''
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#resampling
Resampling:
'''

# generate an index of season dates
dti = pd.date_range(start=winter_start_date, periods=5, freq=six_months)
# convert from DateTimeIndex to PeriodIndex
periods = dti.to_period(freq='6M')

# build the dataset required for analysis
start = pd.to_datetime(winter_start_date_str)
end = pd.to_datetime(long_end_date_str)
index = pd.date_range(start, end, freq='D')
length = len(index)
df = pd.DataFrame(data=np.random.randn(length), index=index)

# upsampling
x = df.resample('H').ffill()

# aggregation
# resample; would be nice to use PeriodIndex; but seems to only support string def
x = df.resample('6MS')
x.count()

# ==============================================================================
'''
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-span-representation
Time span representation:
    Regular intervals of time are represented by Period objects in pandas while 
    sequences of Period objects are collected in a PeriodIndex, which can be created 
    with the convenience function period_range.
'''

# single Period type
p = pd.Period(start_date_str, freq='M')
# which has a start and end time
print(p.start_time, p.end_time)

# range of periods as a PeriodIndex type
pr = pd.period_range(start_date_str, freq='M', periods=3)
# made up of Period objects
p == pr[0]


# ==============================================================================
'''
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#converting-between-representations
Converting between representations
    Timestamped data can be converted to PeriodIndex-ed data using to_period and vice-versa using to_timestamp:
'''

import pdb; pdb.set_trace()
pass