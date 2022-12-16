import pathlib
import pandas as pd

df = pd.read_csv(pathlib.Path().absolute().joinpath('check_paid_bills/amount_ofpaidbills.csv'))
df.dropna()

total_bills = []
paid_bills = []
status = []
indi = []

for index, row in df.iterrows():
    if index == -1:
        break
    total_bills.append(int(row["total_bills"]))
    paid_bills.append(row["paid_bills"])

# main code
data = []
for i in range(len(total_bills)):
    if total_bills[i] in paid_bills:
        status.append("True")
        indi.append(paid_bills.index(total_bills[i]) + 1)
    else:
        status.append("False")
        indi.append("N/A")
    data.append([total_bills[i], paid_bills[i], status[i], indi[i]])

output = pd.DataFrame(data, columns=["total_bills", "paid_bills", "status", "location"])
output.to_csv(pathlib.Path().absolute().joinpath('check_paid_bills/paid_status.csv'), index=False)
