import pandas as pd


'''
https://stackoverflow.com/questions/40468069/merge-two-dataframes-by-index/40468090#40468090

merge: inner join by default:
pd.merge(df1, df2, left_index=True, right_index=True)

join: left join by default:
df1.join(df2)

concat: outer join by default:
pd.concat([df1, df2], axis=1)
'''


# import some data
iris = datasets.load_iris()

# create dataframe
df_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_target = pd.DataFrame(data=iris.target, columns=['target'])

# concatenate
df = pd.concat([df_data, df_target], axis=1)
print(df.head())

print('===============')

