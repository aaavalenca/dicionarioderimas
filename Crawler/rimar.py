import pandas as pd
import unicodedata
import re

# lista_de_consoantes = ['p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 's', 'z', 'ʃ', 'ʒ', 'm', 'n', 'ɲ', 'ŋ', 'l', 'ʎ', 'ɾ', 'j', 'w', 'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'tl', 'tr']
# lista_de_vogais = ['i', 'ɪ', 'e', 'ɛ', 'a', 'ɐ', 'ɨ', 'ʉ', 'o', 'ɔ', 'u', 'ʊ', 'ẽ', 'ã', 'õ', 'ɔ̃', 'ĩ', 'ɐ̃', 'ũ']

def remove_consonants(s):
    lista_de_consoantes = ['p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 's', 'z', 'ʃ', 'ʒ', 'm', 'n', 'ɲ', 'ŋ', 'l', 'ʎ', 'ɾ', 'j', 'w', 'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'tl', 'tr']
    for elem in lista_de_consoantes:
        s = s.replace(elem, '')
    return s

def match_rhyme(tonica, penultima, ultima, df):
    selected_rows = []

    for index, row in df.iterrows():
        col = row['tonica']
        if col == '':
            continue

        val = row[col]
        val = unicodedata.normalize('NFC', val)
        val = val.split('ˈ')[-1]
        val = remove_consonants(val)
        if not (tonica == val):
            continue

        if col == 'antepenultima':
            val = row['penultima']
            val = unicodedata.normalize('NFC', val)
            val = remove_consonants(val)

            if penultima != val:
                continue

            val = row['ultima']
            val = unicodedata.normalize('NFC', val)
            val = remove_consonants(val)            

            if ultima != val:
                continue

        if col == 'penultima':
            val = row['ultima']
            val = unicodedata.normalize('NFC', val)
            val = remove_consonants(val)

            if (ultima != val):
                continue   

        selected_rows.append(row)



    return selected_rows

def read_rhymes():
    df = pd.read_csv("Crawler/database/database.csv", converters={'divisao_list' : eval, 'fonetica_list' : eval})
    x = input("o que você quer rimar?: ")
    row = df[df['palavra'] == x]
    row_stripped = row.loc[row.index[0]]
    tonica_pos = row_stripped["tonica"]
    tonica = row_stripped[tonica_pos].split('ˈ')[-1]
    penultima = row_stripped['penultima']
    ultima = row_stripped['ultima']
    df.fillna('', inplace=True)
    df = df[df['tonica'] == tonica_pos]
    tonica = unicodedata.normalize('NFC', tonica)
    ultima = unicodedata.normalize('NFC', ultima)
    penultima = unicodedata.normalize('NFC', penultima)
  
    tonica = remove_consonants(tonica)
    penultima = remove_consonants(penultima)
    ultima = remove_consonants(ultima)

    # selected_rows = select_rhymed(tonica, penultima, ultima, df)
    selected_rows = match_rhyme(tonica, penultima, ultima, df)
    selected_df = pd.DataFrame(selected_rows)
    print(selected_df)
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)

read_rhymes()