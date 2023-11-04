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
        # se for tônica, tirar indicador
        fonema = fonema.split('ˈ')[-1]
        # verificar a lista de consoantes
        lista_de_consoantes = ['tˌ', 'mw', 'k', 'gwˌ', 'spɾ', 'rj', 'ʎˌ', 'lˌ', 'ɦ', 'blˌ', 'pˌ', 'pɾ', 't', 'zj', 'zˌ', 'bɾj', 'glj', 'tʃj', 'kɾˌ', 'ʎ', 'plj', 'sw', 'bɾ', 'vɾ', 'f', 'ɲ', 'ft', 'tsj', 'x', 'gɾˌ', 'bl', 'klj', 'v', 's', 'p', 'z', 'gˌ', 'fj', 'bj', 'kz', 'ɦw', 'kɾw', 'kɾ', 'w', 'fɾ', 'fˌ', 'tʃˌ', 'g', 'gɾ', 'tɾ', 'pj', 'ɾj', 'dɾ', 'gɾw', 'ɾw', 'mˌ', 'fl', 'ng', 'ps', 'kɾj', 'dɾw', 'tɾj', 'vj', 'dw', 'bˌ', 'tɾˌ', 'ks', 'gj', 'pl', 'ʃj', 'sˌ', 'ɦˌ', 'm', 'tʃ', 'blj', 'pɾw', 'dɾj', 'zw', 'l', 'd', 'lj', 'pɾˌ', 'mj', 'sk', 'kl', 'ˌ', 'st', 'kw', 'j', 'ts', 'kˌ', 'nj', 'ms', 'nˌ', 'bw', 'ɦj', 'dˌ', 'r', 'pw', 'fɾˌ', 'ɾ', 'sj', 'ʃ', 'gw', 'tsˌ', 'cr', 'b', 'nw', 'plˌ', 'ɾˌ', 'kj', 'lw', 'pɾj', 'n', 'fɾj', 'vˌ', 'gl', 'tl']
        for elem in lista_de_consoantes:
            if fonema.startswith(elem):
                fonema = fonema.replace(elem, '')
                continue
            if 'h' in fonema:
                fonema = fonema.replace('h', 'ɦ')
        divisao_fonetica_tratada.append(fonema)
    return divisao_fonetica_tratada

def checar_rima(divisao_fonetica, tonica_fonetica_num, df):
    selected_rows = []
    divisao_fonetica = tratar_fonemas(divisao_fonetica)

    for index, row in df.iterrows():
        divisao_fonetica_row = tratar_fonemas(row['divisao_fonetica'])

        if row['palavra'] == 'tártaro':
            print(divisao_fonetica_row)

        if divisao_fonetica_row[tonica_fonetica_num:] == divisao_fonetica[tonica_fonetica_num:]:
            selected_rows.append(row)
    return selected_rows

def ler_rimas():
    pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)

    # ler a database
    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(current_directory, '..', 'Scrapper/PortalLP/DB/Completo', 'database.csv')
    df = pd.read_csv(relative_path, converters={'divisao_silabica' : eval, 'tonica_silabica_num' : int, 'divisao_fonetica' : eval, 'tonica_fonetica_num' : int})
    # df.fillna('', inplace=True)

    # input do usuário
    x = input("o que você quer rimar?: ")
    x = encontrar_palavra(x, df)[0]

    # verifica se a palavra está na base de dados
    #(adicionar um while x.count > 0 and x não dá match com palavra, tenta dar match pelo final)
    row = df[df['palavra'] == x]
    row_stripped = row.loc[row.index[0]]

    # pega a primeira ocorrência dessa palavra no df (pode ter repetidas)
    row_stripped = row.loc[row.index[0]]

    # pega divisão fonética
    divisao_fonetica = row_stripped["divisao_fonetica"]
    
    # pega posição da tônica
    tonica_fonetica_num = row_stripped["tonica_fonetica_num"]

    # selected_rows = checar_rima(tonica, penultima, ultima, df)
    selected_rows = checar_rima(divisao_fonetica, tonica_fonetica_num, df[df['tonica_fonetica_num'] == tonica_fonetica_num])

    selected_df = pd.DataFrame(selected_rows)
    print(selected_df[['palavra', 'divisao_fonetica']])

ler_rimas()