import csv
import pandas as pd
import ast

def read_rhymes(letter):
    df = pd.read_csv("Crawler/labeled/" + letter + ".csv", converters={'divisao_list' : eval, 'fonetica_list' : eval})
    df2 = df[['palavra', 'fonetica', 'tonica', 'antepenultima', 'penultima', 'ultima']]
    x = input("o que você quer rimar?: ")
    row = df2[df2['palavra'] == x]
    row_stripped = row.loc[row.index[0]]
    tonica_pos = row_stripped["tonica"]
    tonica = row_stripped[tonica_pos]

    print(tonica, tonica_pos)

    print(df2[df2[tonica_pos] == tonica])



read_rhymes("a")