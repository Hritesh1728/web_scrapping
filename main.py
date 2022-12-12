from typing import Union
import httpx
import re
import asyncio
import time
from playwright.async_api import Page, expect,async_playwright



from fastapi import FastAPI,status


app = FastAPI()


@app.get("/",status_code=status.HTTP_404_NOT_FOUND)
def read_root():return {"success": True,"message": "welcome to BandaVala Infosys"}

# @app.post("/fetch_jvvnl",status_code=status.HTTP_200_OK,tags=['electricity fetch'])
# def fetch_jvvnl(kno):
#     return kno

@app.get("/fetch_jvvnl/{kno}")
async def read_item(kno: int):
    req = httpx.get(f"https://www.bijlimitra.com/accountdetailsByKno/{kno}")
    
    return req.json()

@app.get("/check_pincode/{pincode}")
async def pin_code(pincode: int):
    req = httpx.get(f"https://api.postalpincode.in/pincode/{pincode}")
    return req.json()[0]["PostOffice"]

@app.get("/check_weather/{latitude}/{longitude}")
async def weather(latitude: float, longitude: float ):
    req = httpx.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m")
    return req.json()

@app.get("/check_jdvvnl/{kno}")
async def check_jdvvnl_bill_status(kno: int):
    with async_playwright() as p:
        browser = await p.chromium.launch(headless= False )
        page = await browser.new_page()
        await page.goto("https://jansoochna.rajasthan.gov.in/Services/")
        jdvvnl_link = await page.locator("/html/body/div[1]/section/div/div/div[3]/div[2]/div[68]/div/a")
        jdvvnl_link.click()
        await page.locator("Enter_your_K_number")
        
        
        
        # await browser.close()
    return "screenshot.captured"
        