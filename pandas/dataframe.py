
import pandas as pd

def get_data(df):
    month = df['month'] == pd.datetime(2017, 10, 1)
    ins = df['ins_type'] == 'COMM-PHYS'
    hub = df['location'] == 'GASPOOL'
    mask = month & ins & hub

    return df[mask]

data1 = get_data(job1['final_details']['Linear'])
data2 = get_data(job2['final_details']['Linear'])
