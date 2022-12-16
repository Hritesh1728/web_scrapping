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

total_sum = sum(data)
data.sort()
# print(data)
pair_data = []
raw_data = []
max_sum = 10000
max_pair = total_sum // max_sum
# print(max_pair)
exclude = 0

while max_pair and len(data) and (data[len(data) - 1] >= max_sum / 8):
    current_sum = 0
    flag = 0

    for i in range(0, 8):
        if i == 0:
            x = data[len(data)-1-exclude]
        else:
            if (10000 - current_sum) >= data[0]:
                x = max([ele for ele in data if (ele <= 10000 - current_sum)])
            else:
                break
        current_sum += x
        raw_data.append(x)
        data.remove(x)
        if 9995 <= current_sum <= 10000:
            flag = 1
            max_pair = max_pair - 1
            break
    if flag == 0:
        for ele in raw_data:
            data.append(ele)
        data.sort()
        exclude = exclude+1
    if flag == 1:
        print(raw_data)
        raw_data.append(" ")
        raw_data.append(current_sum)
        raw_data.append(10000 - current_sum)
        pair_data.append(list(raw_data))
    raw_data.clear()
    if exclude not in range(0, len(data)+1):
        break

print(data)

pair_data.append([])
pair_data.append(["Data greater than Maximum Sum value"])
pair_data.append(data_greater_max_sum)
pair_data.append([])
pair_data.append(["Data, whose pair cannot be formed!"])
pair_data.append(data)

result = pd.DataFrame(pair_data)
result.to_csv(pathlib.Path().absolute().joinpath('data/pair_data/paired_data.csv'), index=False)
