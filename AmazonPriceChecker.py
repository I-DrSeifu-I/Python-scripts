from colorama import Fore, Back, Style
import requests
from bs4 import BeautifulSoup
import lxml
import time
from datetime import datetime

loggingDestination = "textlog.txt"

def writeoutLog(message, status, logFile):
    timenow = datetime.now()
    current_time = timenow.strftime("%m-%d-%Y | %I:%M:%S %p")
    file = open(logFile, 'a')
    match status:
        case "info":
            print(f"{Fore.BLUE}[INFO][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[INFO][{current_time}] - {message}" + '\n')
        case "success":
            print(f"{Fore.GREEN}[SUCCESS][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[SUCCESS][{current_time}] - {message}" + '\n')
        case "error":
            print(f"{Fore.RED}[ERROR][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[ERROR][{current_time}] - {message}" + '\n')
        case "warning":
            print(f"{Fore.YELLOW}[WARNING][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[WARNING][{current_time}] - {message}" + '\n')
        case _:
            print(f"{Fore.WHITE}[UNKNOWN][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[UNKNOWN][{current_time}] - {message}" + '\n')
    file.close
        

def getAmazonProductInfo(url):
    try:
        getResults = requests.get(url)
        if getResults.status_code == 200:
            writeoutLog("Successfully retrieved info","success", loggingDestination)
        else:
            writeoutLog((f"Did not get info from {url}. Status code = {getResults.status_code}"),"warning", loggingDestination)
    except Exception as error:
        writeoutLog((f"Unable to retrieve info from {url}. Error = {error}"),"error", loggingDestination)


    initialParse = BeautifulSoup(getResults.content, "lxml")

    dataExtractFromParse = BeautifulSoup(initialParse.prettify(), "lxml")

    price = dataExtractFromParse.find("span", {"class": "a-offscreen"}).get_text().strip()
    itemName = dataExtractFromParse.find(id="productTitle").get_text().strip()

    writeoutLog((f"Product Name: {itemName}") , "info", loggingDestination)
    writeoutLog((f"Price : {price}") , "info", loggingDestination)

    hash = productinfo = {
        'productName':itemName,
        'price':price
    }

    return hash

url = "https://www.amazon.com/TracFone-Motorola-Moto-Play-Black/dp/B0CCSZZGT7/ref=sr_1_6?crid=3KUHTOVL8PMCT&dib=eyJ2IjoiMSJ9.6j0kSke5iizAKMrPFcDemETA1faCkHSMvECcyltnFvlZ08NJmUJDoW-QxnEmw2g8vchNslB0xpLay_ZirhVEs9B4gCQsM-u_MUSiFu21Y48QtWciyLN4QpyG4hNnIm0LDzEii5GpJ7QCj6AQgTpCdonl2qu7Ray4i1b_3uYniAD1hBPqas86_-oPmhWqc1on8ACxaEyhJHwCBAmwlmNGZqq9aHddZZSNrq4T2emfQcQ.EePsk7RS0azTLp1pZojo23-MEcSOyHwYcpRwulIoa-o&dib_tag=se&keywords=phone&qid=1717900850&sprefix=phone%2Caps%2C194&sr=8-6"


wantedPrice = 25.00

wantedPriceReached = False

while wantedPriceReached == False:

    time.sleep(2)

    productInfo = getAmazonProductInfo(url)
    priceNumber = float((productInfo.get("price")).replace("$", ""))

    if priceNumber >= wantedPrice:
        writeoutLog((f"Price is still above ${wantedPrice}"), "info", loggingDestination)
    else:
        wantedPriceReached = True
        writeoutLog((f"Price is looking good now. Its below your wanted price: {wantedPrice}"), "success", loggingDestination)


    



