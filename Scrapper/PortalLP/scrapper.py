import requests
from bs4 import BeautifulSoup
import re

def encontrar_seguintes(prefixo, link):
    website_url = requests.get(link).text
    soup = BeautifulSoup(website_url,'lxml')
    hrefs = soup.find_all('a', href=True)
    continuar = False
    sufixo = ""
    for href in hrefs:
        if href.text == 'seguintes':
            print(href['href'])
            sufixo = href['href']
    if sufixo != "":
        continuar = True
    return prefixo + sufixo, continuar

def palavras_da_pagina(link):
    website_url = requests.get(link).text
    soup = BeautifulSoup(website_url,'lxml')
    table = soup.find('table', id='rollovertable')
    table_rows = table.findAll('tr')
    f = []

    for tr in table_rows[1:]:
        # encontrar cada entrada
        entrada = tr.find('td')
        word = re.findall(r'<a(.*?)>(.*?)</a>', str(entrada.a))
        word = (str(entrada.a).replace('\n', '').split("·"))

        # todos os campos do dataframe
        palavra = ""
        categoria = ""
        divisao_silabica = []
        tonica_silabica_num = 0
        divisao_fonetica = []
        tonica_fonetica_num = 0
        tonica_silabica_num = len(word)

        # pega a sílaba tônica da divisão silábica (não necessariamente é igual à fonética,
        # exemplo ab-.ro.ga.tó.ri.o (proparoxítona) vs ab.ɦo.ga.tˈɔ.ɾjʊ (paroxítona)
        num = 0
        for i, syl in enumerate(word):
            if re.search("(.*?)<u>(.*?)</u>(.*?)", syl):
                tonica_silabica_num = tonica_silabica_num - i

        if tonica_silabica_num == 1:
            # último, para poder usar: divisao_silabica[:-1], ou divisao_silabica[:tonica_silabica_num]
            tonica_silabica_num = -1
        elif tonica_silabica_num == 2:
            tonica_silabica_num = -2
        elif tonica_silabica_num == 3:
            tonica_silabica_num = -3

        for td in tr:
            # pegando a divisão fonética
            if num == 1:
                palavra = td.text.strip().replace("·", "")
                divisao = td.text.strip()
                divisao_silabica = re.split("·|-", divisao)
            if num == 2:
                categoria = td.text.strip()
            if num == 3:
                fonetica = td.text
                if (' ou ') in fonetica:
                    fonetica = fonetica.split(' ou ')[0]
                
                fonetica = fonetica.strip()
                divisao_fonetica = fonetica.split(".")
                if divisao_fonetica:
                    for i, fon in enumerate(divisao_fonetica[::-1]):
                        # a posição da tônica fonética
                        if "ˈ" in fon:
                            tonica_fonetica_num = -(i + 1)
            num = num + 1

        f.append([palavra, categoria, divisao_silabica, tonica_silabica_num, divisao_fonetica, tonica_fonetica_num])

    return f

# print(palavras_da_pagina('http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=rjx&act=list&letter=w'))