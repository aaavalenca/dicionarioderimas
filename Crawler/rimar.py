import pandas as pd
import unicodedata

def select_rhymed(tonica, penultima, ultima, row_stripped, df):
    selected_rows = []
    for index, row in df.iterrows():
        col = row['tonica']
        if col == '':
            continue
        val = row[col]
        val = unicodedata.normalize('NFC', val)
        if not (tonica == val.split('ˈ')[-1]):
            continue

        if col == 'antepenultima':
            val = row['penultima']
            val = unicodedata.normalize('NFC', val)
            print(val)
            # fazer um regex para tirar as consoantes
            if not (penultima[1:] == val[1:]):
                continue
            val = row['ultima']
            val = unicodedata.normalize('NFC', val)
            print(val)
            if not (ultima[1:] == val[1:]):
                continue
        if col == 'penultima':
            val = row['ultima']
            val = unicodedata.normalize('NFC', val)
            if not (ultima[1:] == val[1:]):
                continue
            print(ultima, val)

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

    selected_rows = select_rhymed(tonica, penultima, ultima, row_stripped, df)
    selected_df = pd.DataFrame(selected_rows)
    print(selected_df)

read_rhymes()