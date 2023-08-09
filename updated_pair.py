import pathlib
import numpy as np
import pandas as pd

df1 = pd.read_csv(pathlib.Path().absolute().joinpath('data/pair_data/amount.csv'))
df1.drop_duplicates()
df1.dropna()
data = []
data_greater_max_given_sum = []
for index, row in df1.iterrows():
    if index == -1:
        break
    if row["Amount"] <= 10000:
        data.append(int(row["Amount"]))
    else:
        data_greater_max_given_sum.append(row["Amount"])
# print(data)


def find_subsets(arr, target):
    # Create an empty dataframe to store the subsets
    df = pd.DataFrame(columns=range(len(arr)))
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Create a new column for each element
        df[i] = np.NaN

        # Iterate through each row in the dataframe
        for j in range(len(df)):
            # Check if the current element can be added to the subset without exceeding the target sum
            if df.iloc[j].sum() + arr[i] <= target:
                # Add the current element to the subset
                df.iloc[j, i] = arr[i]

            # If the current element cannot be added, create a new row for a new subset
            else:
                df = df.append(pd.Series(index=range(len(arr))), ignore_index=True)

    # Remove all rows that have any NaN values (subsets that were not filled)
    df = df.dropna(how='any')

    # Return the dataframe of subsets
    return df


arr = [1, 2, 3, 4]
target = 5
print(find_subsets(arr, target))
