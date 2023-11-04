import pandas as pd
import re

def pegar_fonemas():
    df = pd.read_csv("../Scapper/PortalLP/DB/database.csv", converters={'divisao_list' : eval, 'fonetica_list' : eval})
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