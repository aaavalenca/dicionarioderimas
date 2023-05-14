import pandas as pd
import unicodedata

def read_rhymes():
    df = pd.read_csv("Crawler/database/database.csv", converters={'divisao_list' : eval, 'fonetica_list' : eval})
    df2 = df[['palavra', 'fonetica', 'tonica', 'antepenultima', 'penultima', 'ultima']]
    x = input("o que você quer rimar?: ")
    row = df2[df2['palavra'] == x]
    row_stripped = row.loc[row.index[0]]
    tonica_pos = row_stripped["tonica"]
    tonica = row_stripped[tonica_pos].split('ˈ')[-1]
    print(tonica_pos, tonica)
    df2.fillna('', inplace=True)
    df2 = df2[df['tonica'] == tonica_pos]
    selected_rows = []
    tonica = unicodedata.normalize('NFC', tonica)

    for index, row in df2.iterrows():
        col = row['tonica']
        if col == '':
            continue
        val = row[col]
        val = unicodedata.normalize('NFC', val)
        if not (tonica in val):
            continue
        selected_rows.append(row)

    selected_df = pd.DataFrame(selected_rows)
    print(selected_df)


read_rhymes()