from collections import defaultdict
import os
import difflib
import pandas as pd
import unicodedata
from fonemas import fonema_num

def encontrar_palavra(w, df):
    w = w.lower()
    return difflib.get_close_matches(w, df.palavra.astype(str), n=50, cutoff=.6)

def tratar_fonemas(divisao_fonetica):
    divisao_fonetica_tratada = []
    for fonema in divisao_fonetica:
        fonema = unicodedata.normalize('NFC', fonema)
        fonema = fonema.split('ˈ')[-1]
        lista_de_consoantes = ['tˌ', 'mw', 'k', 'gwˌ', 'spɾ', 'rj', 'ʎˌ', 'lˌ', 'ɦ', 'blˌ', 'pˌ', 'pɾ', 't', 'zj', 'zˌ', 'bɾj', 'glj', 'tʃj', 'kɾˌ', 'ʎ', 'plj', 'sw', 'bɾ', 'vɾ', 'f', 'ɲ', 'ft', 'tsj', 'x', 'gɾˌ', 'bl', 'klj', 'v', 's', 'p', 'z', 'gˌ', 'fj', 'bj', 'kz', 'ɦw', 'kɾw', 'kɾ', 'w', 'fɾ', 'fˌ', 'tʃˌ', 'g', 'gɾ', 'tɾ', 'pj', 'ɾj', 'dɾ', 'gɾw', 'ɾw', 'mˌ', 'fl', 'ng', 'ps', 'kɾj', 'dɾw', 'tɾj', 'vj', 'dw', 'bˌ', 'tɾˌ', 'ks', 'gj', 'pl', 'ʃj', 'sˌ', 'ɦˌ', 'm', 'tʃ', 'blj', 'pɾw', 'dɾj', 'zw', 'l', 'd', 'lj', 'pɾˌ', 'mj', 'sk', 'kl', 'ˌ', 'st', 'kw', 'j', 'ts', 'kˌ', 'nj', 'ms', 'nˌ', 'bw', 'ɦj', 'dˌ', 'r', 'pw', 'fɾˌ', 'ɾ', 'sj', 'ʃ', 'gw', 'tsˌ', 'cr', 'b', 'nw', 'plˌ', 'ɾˌ', 'kj', 'lw', 'pɾj', 'n', 'fɾj', 'vˌ', 'gl', 'tl']
        for elem in lista_de_consoantes:
            if fonema.startswith(elem):
                fonema = fonema.replace(elem, '')
                continue
            if 'h' in fonema:
                fonema = fonema.replace('h', 'ɦ')
        divisao_fonetica_tratada.append(fonema)
    return divisao_fonetica_tratada

def checar_similaridade(list1, list2):
    matching_count = sum(x == y for x, y in zip(list1, list2))
    return matching_count

def checar_rima(divisao_fonetica, tonica_fonetica_num, df):
    selected_rows = []
    divisao_fonetica_tratada = tratar_fonemas(divisao_fonetica)
    for _, row in df.iterrows():
        divisao_fonetica_row = tratar_fonemas(row['divisao_fonetica'])
        if divisao_fonetica_row[tonica_fonetica_num:] == divisao_fonetica_tratada[tonica_fonetica_num:]:
            selected_rows.append(row)
            row['prioridade'] = checar_similaridade(divisao_fonetica[tonica_fonetica_num:], row['divisao_fonetica'][tonica_fonetica_num:])
    return selected_rows

def ler_rimas(x):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(current_directory, '..', 'PortalLP/DB/Completo', 'database.csv')
    df = pd.read_csv(relative_path, converters={'divisao_silabica' : eval, 'tonica_silabica_num' : int, 'divisao_fonetica' : eval, 'tonica_fonetica_num' : int})
    x = encontrar_palavra(x, df)[0]
    df['prioridade'] = 0

    row = df[df['palavra'] == x]
    row_stripped = row.loc[row.index[0]]
    row_stripped = row.loc[row.index[0]]
    divisao_fonetica = row_stripped["divisao_fonetica"]
    tonica_fonetica_num = row_stripped["tonica_fonetica_num"]
    selected_rows = checar_rima(divisao_fonetica, tonica_fonetica_num, df[df['tonica_fonetica_num'] == tonica_fonetica_num])
    selected_df = pd.DataFrame(selected_rows)
    selected_df.sort_values(by='categoria', inplace=True)
    return selected_df[['palavra', 'categoria', 'prioridade']].sort_values(by='prioridade', ascending=False)

ler_rimas('parente')