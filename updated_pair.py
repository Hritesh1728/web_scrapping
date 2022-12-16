import pathlib

import pandas as pd

df = pd.read_csv(pathlib.Path().absolute().joinpath('data/pair_data/amount.csv'))
df.drop_duplicates()
df.dropna()
data = []
data_greater_max_sum = []
for index, row in df.iterrows():
    if index == -1:
        break
    if row["Amount"] <= 10000:
        data.append(int(row["Amount"]))
    else:
        data_greater_max_sum.append(row["Amount"])



