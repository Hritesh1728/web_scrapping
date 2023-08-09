import pathlib
import time
import httpx
from playwright.sync_api import Playwright, sync_playwright

import pandas as pd


def automate_jodhpur():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://jansoochna.rajasthan.gov.in/Services/", wait_until="load", timeout=60000)

        page.get_by_role("link", name="68.) Know about your Electricity Bill Payment Information - JDVVNL").click()
        page.get_by_placeholder("Enter your K number").click()
        page.get_by_text("Enter your K number").wait_for(timeout=60000)

        # csv importing file
        print('welcome to JDVVNL Bill Status')
        df = pd.read_csv(pathlib.Path().absolute().joinpath('data/jodhpur/source.csv'))
        df.drop_duplicates()
        df.dropna()

        # output = pd.DataFrame({})

        data = {}
        output = []
        for index, row in df.iterrows():
            if index == -1:
                break
            print(f'Working for {row["kno"]} with ID: {index}')
            page.get_by_placeholder("Enter your K number").fill(f'{row["kno"]}')

            page.get_by_role("button", name="खोजें").click()
            data["k_number"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(1)").inner_text()
            data["name"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(2)").inner_text()
            data["address"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(3)").inner_text()
            data["account_number"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(4)").inner_text()
            data["bill_number"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(5)").inner_text()
            data["receipt_number"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(6)").inner_text()
            data["billing_month"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(7)").inner_text()
            data["payment_mode"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(8)").inner_text()
            data["reference_number"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(9)").inner_text()
            data["issue_date"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(10)").inner_text()
            data["issue_bank"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(11)").inner_text()
            data["bill_amount_(rs)"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(12)").inner_text()
            data["receipt_date"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(13)").inner_text()
            output.append(list(data.values()))

        result = pd.DataFrame(output, columns=list(data.keys()))
        result.to_csv(pathlib.Path().absolute().joinpath('data/jodhpur/result.csv'), index=False)

        print('Bye')

        # ---------------------
        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)


def automate_ajmer():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://jansoochna.rajasthan.gov.in/Services/", wait_until="load", timeout=60000)

        page.get_by_role("link", name="69.) Know about your Electricity Bill Payment Information - AVVNL").click()
        page.get_by_placeholder("Enter your K number").click()
        page.get_by_text("Enter your K number").wait_for(timeout=60000)

        # csv importing file
        print('welcome to AVVNL Bill Status')
        df = pd.read_csv(pathlib.Path().absolute().joinpath('data/ajmer/source.csv'))
        df.drop_duplicates()
        df.dropna()

        # output = pd.DataFrame({})

        data1 = {}
        output = []
        for index, row in df.iterrows():
            if index == -1:
                break
            print(f'Working for {row["kno"]} with ID: {index}')
            page.get_by_placeholder("Enter your K number").fill(f'{row["kno"]}')

            page.get_by_role("button", name="खोजें").click()
            page.wait_for_timeout(3000)

            data1["k_number"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(1)").inner_text()
            data1["name"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(2)").inner_text()
            data1["address"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(3)").inner_text()
            data1["account_number"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(4)").inner_text()
            data1["bill_number"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(5)").inner_text()
            data1["receipt_number"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(6)").inner_text()
            data1["billing_month"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(7)").inner_text()
            data1["payment_mode"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(8)").inner_text()
            data1["reference_number"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(9)").inner_text()
            data1["issue_date"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(10)").inner_text()
            data1["issue_bank"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(11)").inner_text()
            data1["bill_amount_(rs)"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(12)").inner_text()
            data1["receipt_date"] = page.locator(
                "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(13)").inner_text()
            output.append(list(data1.values()))

        result = pd.DataFrame(output, columns=list(data1.keys()))
        result.to_csv(pathlib.Path().absolute().joinpath('data/ajmer/result.csv'), index=False)

        print('Bye')

        # ---------------------
        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)


def check_jvvnl_bills():
    print('welcome to JVVNL Bill Status')
    df = pd.read_csv(pathlib.Path().absolute().joinpath('data/jaipur/source.csv'))
    df.drop_duplicates()
    df.dropna()
    data = []
    for index, row in df.iterrows():
        if index == -1:
            break
        print(f'Working for {row["kno"]} with ID: {index}')
        time.sleep(1)
        client = httpx.Client(http2=True)
        r = client.get(f'https://www.bijlimitra.com/accountdetailsByKno/{row["kno"]}', timeout=50)
        if r.status_code == httpx.codes.OK:
            # if r.json() == 1:
            #     data.append(list(f'Invalid kno = {row["kno"]}'))
            #     continue
            data.append(r.json()[0])
        client.close()
        result = pd.DataFrame(data)
        result.to_csv(pathlib.Path().absolute().joinpath('data/jaipur/result.csv'), index=False)
        print('Result Saved')
    print('Bye')


flag = 1
while flag:
    board = input(
        "Choose the board as 1 or 2 or 3 whose indication are below:-\n "
        "1. Ajmer Board \n 2. Jaipur Board \n 3. Jodhpur Board \n Your Input:- ")

    if board == '1':
        flag = 0
        automate_ajmer()
    elif board == '2':
        flag = 0
        check_jvvnl_bills()
    elif board == '3':
        flag = 0
        automate_jodhpur()
    else:
        print("------Input only from 1,2,3 for the respective boards------------------")
