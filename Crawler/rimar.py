import pandas as pd
import unicodedata
import re

# lista_de_consoantes = ['p', 'b', 't', 'd', 'k', 'g', 'f', 'v', 's', 'z', 'ʃ', 'ʒ', 'm', 'n', 'ɲ', 'ŋ', 'l', 'ʎ', 'ɾ', 'j', 'w', 'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'tl', 'tr']
# lista_de_vogais = ['i', 'ɪ', 'e', 'ɛ', 'a', 'ɐ', 'ɨ', 'ʉ', 'o', 'ɔ', 'u', 'ʊ', 'ẽ', 'ã', 'õ', 'ɔ̃', 'ĩ', 'ɐ̃', 'ũ']

def remove_consonants(s):
    # verificar a lista de consoantes
    lista_de_consoantes = ['tˌ', 'mw', 'k', 'gwˌ', 'spɾ', 'rj', 'ʎˌ', 'lˌ', 'ɦ', 'blˌ', 'pˌ', 'pɾ', 't', 'zj', 'zˌ', 'bɾj', 'glj', 'tʃj', 'kɾˌ', 'ʎ', 'plj', 'sw', 'bɾ', 'vɾ', 'f', 'ɲ', 'ft', 'tsj', 'x', 'gɾˌ', 'bl', 'klj', 'v', 's', 'p', 'z', 'gˌ', 'fj', 'bj', 'kz', 'ɦw', 'kɾw', 'kɾ', 'w', 'fɾ', 'fˌ', 'tʃˌ', 'g', 'gɾ', 'tɾ', 'pj', 'ɾj', 'dɾ', 'gɾw', 'ɾw', 'mˌ', 'fl', 'ng', 'ps', 'kɾj', 'dɾw', 'tɾj', 'vj', 'dw', 'bˌ', 'tɾˌ', 'ks', 'gj', 'pl', 'ʃj', 'sˌ', 'ɦˌ', 'm', 'tʃ', 'blj', 'pɾw', 'dɾj', 'zw', 'l', 'd', 'lj', 'pɾˌ', 'mj', 'sk', 'kl', 'ˌ', 'st', 'kw', 'j', 'ts', 'kˌ', 'nj', 'ms', 'nˌ', 'bw', 'ɦj', 'dˌ', 'r', 'pw', 'fɾˌ', 'ɾ', 'sj', 'ʃ', 'gw', 'tsˌ', 'cr', 'b', 'nw', 'plˌ', 'ɾˌ', 'kj', 'lw', 'pɾj', 'n', 'fɾj', 'vˌ', 'gl', 'tl']
    for elem in lista_de_consoantes:
        if s.startswith(elem):
            s = s.replace(elem, '')
            continue
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

    selected_rows = match_rhyme(tonica, penultima, ultima, df)
    selected_df = pd.DataFrame(selected_rows)
    print(selected_df)

# read_rhymes()

def get_phonemes():
    df = pd.read_csv("Crawler/database/database.csv", converters={'divisao_list' : eval, 'fonetica_list' : eval})
    unique_antepenultima = df['antepenultima'].unique()
    unique_penultima = df['penultima'].unique()
    unique_ultima = df['ultima'].unique()
    unique_antepenultima = unique_antepenultima.tolist()
    unique_antepenultima.extend(unique_penultima.tolist())
    unique_antepenultima.extend(unique_ultima.tolist())

    cons_list = []
    vog_list = []
    for foneme in unique_antepenultima:
        if type(foneme) == str:
            print(foneme)
            if foneme == 'dʃ':
                continue
            foneme = foneme.replace("ˈ", "")
            split = re.split(r'(?=a|e|i|o|u|ɪ|ɔ|ɐ̃|ə|ɛ|ɐ|ʊ|ɨ̃|ʒ)', foneme)
            consonant = split[0]
            vogal = split[1]

            cons_list.append(consonant)
            vog_list.append(vogal)

    cons_list = list(set(cons_list))
    vog_list = list(set(vog_list))

    print(cons_list)
    print(vog_list)

    # for foneme in final_list:
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)

read_rhymes()