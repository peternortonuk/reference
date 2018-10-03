import pandas as pd
import datetime as dt

# create a range of dates
index = pd.date_range(start='01-May-2018', periods=20)

# create a single date; all three are equivalent
single_date1 = pd.Timestamp('05-May-2018')
single_date2 = pd.to_datetime('05-May-2018')
x = dt.date(2018, 5, 5)
single_date3 = pd.to_datetime(x)

# compare a single date with an index of dates
mask = index > single_date3

pass
