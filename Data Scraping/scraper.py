import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
import time

baseLink = "https://sihtasutus.ut.ee"
homePage = "/scholarship-competitions"

#open the main page of scholarships
resPage = requests.get(baseLink+homePage)
htmlPage = BeautifulSoup(resPage.text, "html.parser")

#get the links of the pages of each scholarships
scholarshipsUrls = [linkDiv.find("a")["href"] for linkDiv in htmlPage.find_all("div", class_ = "options")]

for scholarhip in scholarshipsUrls:
    url = baseLink+scholarhip
    scholarhipPage = requests.get(url)
    pageBs = BeautifulSoup(resPage.text, "html.parser")
    
    fields = pageBs.find("div", class_ = "field main-content")

    print(pageBs)
    