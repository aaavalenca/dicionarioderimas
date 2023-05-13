import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html
import re

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
        tonica_num = len(word)
        count = 0

        for syl in word:
            if re.search("<b>(.*?)</b>", syl) :
                tonica_num = tonica_num - count
            count = count + 1

        palavra = ""
        divisao_list = []
        divisao = ""
        categoria = ""
        fonetica_list = []
        fonetica = ""
        tonica = ""
        num = 0
        antepenultima = ""
        penultima = ""
        ultima = ""
        
        if tonica_num == 1:
            tonica = "ultima"
        elif tonica_num == 2:
            tonica = "penultima"
        elif tonica_num == 3:
            tonica = "antepenultima"

        for td in tr:
            if num == 1:
                palavra = td.text.strip().replace("·", "")
                divisao = td.text.strip()
                divisao_list = re.split("·|-", divisao)
            if num == 2:
                categoria = td.text.strip()
            if num == 3:
                fonetica = td.text.strip()
                fonetica_list = fonetica.split(".")
                if fonetica_list:
                    for i, fon in enumerate(fonetica_list[::-1]):
                        if i == 0:
                            ultima = fon
                        elif i == 1:
                            penultima = fon
                        elif i == 2: 
                            antepenultima = fon
                        else:
                            break
            num = num + 1
            # print(td.text.strip())
            # print("****")
        f.append([palavra, divisao_list, divisao, categoria, fonetica_list, fonetica, tonica_num, tonica, antepenultima, penultima, ultima])
        # time.sleep(3)

    return f