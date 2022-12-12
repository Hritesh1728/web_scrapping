import pathlib
import time
from playwright.sync_api import Playwright, sync_playwright, expect
import csv
import pandas as pd


def automate_jodhpur():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://jansoochna.rajasthan.gov.in/Services/")

        page.get_by_role("link", name="68.) Know about your Electricity Bill Payment Information - JDVVNL").click()
        page.get_by_placeholder("Enter your K number").click()

        # csv impoting file
        print('welcome to JDVVNL Bill Status')
        df = pd.read_csv(pathlib.Path().absolute().joinpath('data/source.csv'))
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
            time.sleep(5)
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
        result.to_csv(pathlib.Path().absolute().joinpath('data/result.csv'), index=False)

        print('Bye')

        # ---------------------
        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)


automate_jodhpur()
# def automate_ajmer():
#     def run(playwright: Playwright) -> None:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://jansoochna.rajasthan.gov.in/Services/")
#
#         page.get_by_role("link", name="69.) Know about your Electricity Bill Payment Information - AVVNL").click()
#         page.get_by_placeholder("Enter your K number").click()
#
#         # csv impoting file
#         print('welcome to AVVNL Bill Status')
#         df = pd.read_csv(pathlib.Path().absolute().joinpath('data/source.csv'))
#         df.drop_duplicates()
#         df.dropna()
#
#         # output = pd.DataFrame({})
#
#         data = {}
#         output = []
#         for index, row in df.iterrows():
#             if index == -1:
#                 break
#             print(f'Working for {row["kno"]} with ID: {index}')
#             page.get_by_placeholder("Enter your K number").fill(f'{row["kno"]}')
#             time.sleep(5)
#             page.get_by_role("button", name="खोजें").click()
#
#             data["k_number"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(1)").inner_text()
#             data["name"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(2)").inner_text()
#             data["address"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(3)").inner_text()
#             data["account_number"] = page.locator(
#                 "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(4)").inner_text()
#             data["bill_number"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(5)").inner_text()
#             data["receipt_number"] = page.locator(
#                 "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(6)").inner_text()
#             data["billing_month"] = page.locator(
#                 "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(7)").inner_text()
#             data["payment_mode"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(8)").inner_text()
#             data["reference_number"] = page.locator(
#                 "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(9)").inner_text()
#             data["issue_date"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(10)").inner_text()
#             data["issue_bank"] = page.locator("#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(11)").inner_text()
#             data["bill_amount_(rs)"] = page.locator(
#                 "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(12)").inner_text()
#             data["receipt_date"] = page.locator(
#                 "#tblResult_0 > tbody > tr:nth-child(1) > td:nth-child(13)").inner_text()
#             output.append(list(data.values()))
#
#         result = pd.DataFrame(output, columns=list(data.keys()))
#         result.to_csv(pathlib.Path().absolute().joinpath('data/result.csv'), index=False)
#
#         print('Bye')
#
#         # ---------------------
#         context.close()
#         browser.close()
#
#     with sync_playwright() as playwright:
#         run(playwright)
