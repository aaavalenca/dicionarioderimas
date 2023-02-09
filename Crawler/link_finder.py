import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html
import re
import time

def find_seguintes(preffix, link):
    website_url = requests.get(link).text
    soup = BeautifulSoup(website_url,'lxml')
    hrefs = soup.find_all('a', href=True)
    go_ahead = False
    suffix = ""
    for href in hrefs:
        if href.text == 'seguintes':
            print(href['href'])
            suffix = href['href']
    if suffix != "":
        go_ahead = True
    return preffix + suffix, go_ahead

def get_entries_page(link):
    website_url = requests.get(link).text
    soup = BeautifulSoup(website_url,'lxml')
    table = soup.find('table', id='rollovertable')
    table_rows = table.findAll('tr')
    f = []

    for tr in table_rows[1:]:
        entry = tr.find('td')
        word = re.findall(r'<a(.*?)>(.*?)</a>', str(entry.a))
        word = (str(entry.a).split("·"))
        tonic = len(word)
        count = 0

        for syl in word:
            if re.search("<b>(.*?)</b>", syl) :
                tonic = tonic - count
            count = count + 1

        palavra = ""
        divisao = []
        categoria = ""
        fonetica = []        
        num = 0
        for td in tr:
            if num == 1:
                palavra = td.text.strip().replace("·", "")
                divisao = re.split("·|-", td.text.strip())
            if num == 2:
                categoria = td.text.strip()
            if num == 3:
                fonetica = td.text.strip().split(".")
            num = num + 1
            # print(td.text.strip())
            # print("****")
        f.append([palavra, divisao, categoria, fonetica, tonic])
        # time.sleep(3)

    return f