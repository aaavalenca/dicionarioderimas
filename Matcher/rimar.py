#implementar paroxítona real

import pandas as pd
import unicodedata
import re
from fonemas import fonema_num

def tratar_fonema(fonema):
    fonema = unicodedata.normalize('NFC', fonema)
    # se for tônica, tirar indicador
    fonema = fonema.split('ˈ')[-1]
    # verificar a lista de consoantes
    lista_de_consoantes = ['tˌ', 'mw', 'k', 'gwˌ', 'spɾ', 'rj', 'ʎˌ', 'lˌ', 'ɦ', 'blˌ', 'pˌ', 'pɾ', 't', 'zj', 'zˌ', 'bɾj', 'glj', 'tʃj', 'kɾˌ', 'ʎ', 'plj', 'sw', 'bɾ', 'vɾ', 'f', 'ɲ', 'ft', 'tsj', 'x', 'gɾˌ', 'bl', 'klj', 'v', 's', 'p', 'z', 'gˌ', 'fj', 'bj', 'kz', 'ɦw', 'kɾw', 'kɾ', 'w', 'fɾ', 'fˌ', 'tʃˌ', 'g', 'gɾ', 'tɾ', 'pj', 'ɾj', 'dɾ', 'gɾw', 'ɾw', 'mˌ', 'fl', 'ng', 'ps', 'kɾj', 'dɾw', 'tɾj', 'vj', 'dw', 'bˌ', 'tɾˌ', 'ks', 'gj', 'pl', 'ʃj', 'sˌ', 'ɦˌ', 'm', 'tʃ', 'blj', 'pɾw', 'dɾj', 'zw', 'l', 'd', 'lj', 'pɾˌ', 'mj', 'sk', 'kl', 'ˌ', 'st', 'kw', 'j', 'ts', 'kˌ', 'nj', 'ms', 'nˌ', 'bw', 'ɦj', 'dˌ', 'r', 'pw', 'fɾˌ', 'ɾ', 'sj', 'ʃ', 'gw', 'tsˌ', 'cr', 'b', 'nw', 'plˌ', 'ɾˌ', 'kj', 'lw', 'pɾj', 'n', 'fɾj', 'vˌ', 'gl', 'tl']
    for elem in lista_de_consoantes:
        if fonema.startswith(elem):
            fonema = fonema.replace(elem, '')
            continue
    return fonema

def checar_rima(tonica_input, penultima_input, ultima_input, df):
    selected_rows = []

    for index, row in df.iterrows():
        # decobrindo a tônica (antepenúltima, penúltima ou última)
        tonica_pos_database = row['tonica']
        if tonica_pos_database == '':
            continue
        
        # descobrindo o fonema da tônica daquela palavra
        tonica_database = tratar_fonema(row[tonica_pos_database])

        if tonica_pos_database == 'antepenultima':
            # checa se a tônica é igual
            if tonica_database != tonica_input:
                continue

            penultima_database = tratar_fonema(row['penultima'])

            # checa se a penúltima sílaba é igual
            if penultima_database != penultima_input:
                continue

            ultima_database = tratar_fonema(row['ultima'])

            # checa se a última é igual
            if fonema_num(ultima_database) != fonema_num(ultima_input):
                continue

        if tonica_pos_database == 'penultima':
            # checa se a tônica bate

            if fonema_num(tonica_database) != fonema_num(tonica_input):
                continue

            ultima_database = tratar_fonema(row['ultima'])

            # checa se a última bate
            if fonema_num(ultima_database) != fonema_num(ultima_input):
                continue

        else:
            if fonema_num(tonica_database) != fonema_num(tonica_input):
                continue

        selected_rows.append(row)

    return selected_rows

def ler_rimas():
    pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)

    # ler a database
    df = pd.read_csv("/Users/aaav/Documents/Coding/Dicionario de Rimas/Crawler/database/database.csv", converters={'divisao_list' : eval, 'fonetica_list' : eval})
    df.fillna('', inplace=True)

    # input do usuário
    x = input("o que você quer rimar?: ")

    # verifica se a palavra está na base de dados
    #(adicionar um while x.count > 0 and x não dá match com palavra, tenta dar match pelo final)
    row = df[df['palavra'] == x]

    # pega a primeira ocorrência dessa palavra no df (pode ter repetidas)
    row_stripped = row.loc[row.index[0]]

    # pega a posição da tônica (se é penúltima, antepenúltima ou última)
    tonica_pos = row_stripped["tonica"]

    # # pega a tônica de acordo com sua posição, retira o indicador de tônica
    
    # pega a tônica de acordo com sua posição, retira o indicador de tônica
    tonica = tratar_fonema(row_stripped[tonica_pos])

    # extrai a penúltima
    penultima = tratar_fonema(row_stripped['penultima'])

    # # extrai a última
    ultima = tratar_fonema(row_stripped['ultima'])

    # com a posição da tônica, sabemos se é oxítona, paroxítona,
    # ou proparoxítona; filtramos o df de acordo
    df = df[df['tonica'] == tonica_pos]

    selected_rows = checar_rima(tonica, penultima, ultima, df)

    selected_df = pd.DataFrame(selected_rows)
    print(selected_df[['palavra', 'fonetica_list', 'tonica']])

ler_rimas()