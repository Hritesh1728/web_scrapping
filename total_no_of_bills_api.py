from fastapi import FastAPI
import pandas as pd
from fastapi import HTTPException, File, UploadFile, Response
from openpyxl import Workbook

app = FastAPI()


@app.post("/")
async def bills_paid(file: UploadFile = File(...)):
    # code for getting a data in excel format
    # if file.content_type != "text/xlsx":
    #     raise HTTPException(status_code=400, detail="Invalid file type. Please provide a xlsx Excel sheet.")
    df = pd.read_excel(file.file, sheet_name=["Sheet1", "Sheet2"])
    df["Sheet1"].dropna()
    df["Sheet1"].drop_duplicates()
    df["Sheet2"].dropna()

    # Main Logic Code
    # Variables
    ref_no_s1 = []
    ref_no_s2 = {}
    output_data = []

    # Logic Code
    for index, row in df["Sheet1"].iterrows():
        if index == -1:
            break
        ref_no_s1.append(row["REF NO"])

    for index, row in df["Sheet2"].iterrows():
        if index == -1:
            break
        if row["CARD_REF_NUM"] in ref_no_s1:
            ref_no_s2.setdefault(row["CARD_REF_NUM"], []).append(int(row["BILL_AMT"]))

    for ref_no in ref_no_s1:
        if ref_no not in ref_no_s2.keys():
            ref_no_s2.setdefault(ref_no, []).append("Not Available")

    for ele in ref_no_s2.keys():
        total_sum = 0
        for j in range(len(ref_no_s2[ele])):
            if ref_no_s2[ele][j] != "Not Available":
                total_sum = total_sum + ref_no_s2[ele][j]
            if j == 0 and len(ref_no_s2[ele]) != 1:
                output_data.append([ele, ref_no_s2[ele][j], " "])
            elif j == 0 and len(ref_no_s2[ele]) == 1:
                output_data.append([ele, ref_no_s2[ele][j], total_sum])
            elif j == len(ref_no_s2[ele]) - 1:
                output_data.append([" ", ref_no_s2[ele][j], total_sum])
            else:
                output_data.append([" ", ref_no_s2[ele][j], " "])
        output_data.append([])

    output = pd.DataFrame(output_data, columns=["CARD_REF_NUM", "BILL_AMT", "TOTAL_AMT"])
    csv = output.to_csv(index=False)

    # output.to_excel(file.file, index=False, header=True, sheet_name='Sheet3')
    #
    #
    # output as downloadable file
    headers = {"Content-Disposition": "attachment;filename=output_of_total_bill_finder.csv"}
    return Response(content=csv, headers=headers)
