import pandas as pd
import unicodedata

def fonema_simples(tonica, fonema):
    if fonema == 'i' or fonema == 'ɨ' or fonema == 'uj' or fonema == 'ɪ' or fonema == 'ɨ̃' or fonema == 'ə' or fonema == 'ə̃' or fonema == 'ab' or fonema == 'ad' or fonema == 'də' or fonema == 'amĩ' or fonema == 'ujʃ':
        return 'i'
    elif fonema == 'e':
        return 'e'
    elif fonema == 'ej':
        if tonica == -1:
            return 'ej'
        else:
            return 'e'
    elif fonema == 'ẽj':
        if tonica == -1:
            return 'êi'
        else:
            return 'e'
    elif fonema == 'ɛ' or fonema == 'er' or fonema == 'erj':
        return 'é'
    elif fonema == 'a' or fonema == 'ɐ':
        return 'a'
    elif fonema == 'o' or fonema == 'oh' or fonema == 'ow' or fonema == 'ɔo':
        return 'ô'
    elif fonema == 'oj':
        if tonica == -1:
            return 'ôi'
        else:
            return 'ô'
    elif fonema == 'ɔ' or fonema == 'ɔw':
        return 'ó'
    elif fonema == 'ɔj':
        if tonica == -1:
            return 'ói'
        else:
            return 'ó'
    elif fonema == 'u' or fonema == 'uw' or fonema == 'ʊ' or fonema == 'ʊj':
        return 'u'
    elif fonema == 'ẽ' or fonema == 'ɛ̃':
        return 'ẽ'
    elif fonema == 'ũn':
        return 'un'
    elif fonema == 'ã' or fonema == 'ɐ̃' or fonema == 'ɐ̃m':
        return 'ã'
    elif fonema == 'õ' or fonema == 'ɔ̃':
        return 'õ'
    elif fonema == 'ĩ' or fonema == 'ĩn' or fonema == 'ĩŋ':
        return 'ĩ'
    elif fonema == 'ũ' or fonema == 'ũj':
        return 'ũ'
    elif fonema == 'ɐ̃j' or fonema == 'ãj' or fonema == 'ãj':
        return 'ãe'
    elif fonema == 'aw' or fonema == 'ãw' or fonema == 'awj':
        return 'au'
    elif fonema == 'ew' or fonema == 'ẽw':
        return 'eu'
    elif fonema == 'ɛw':
        return 'éu'
    elif fonema == 'iw':
        return 'iu'
    elif fonema == 'aj' or fonema == 'ɐj' or fonema == 'aks' or fonema == "ajj":
        return 'ai'
    elif fonema == 'ij' or fonema == 'ɪj':
        return 'is'
    elif fonema == 'ɛj':
        if tonica == -1:
            return 'éi'
        else:
            return 'é'
    elif fonema == 'ɐ̃w':
        return 'ão'
    elif fonema == 'õj':
        if tonica == -1:
            return 'õe'
        else:
            return 'ô'
    elif fonema == 'ẽj':
        if tonica == -1:
            return 'em'
        else:
            return 'e'
    else:
        return ''

# def fonema_simple(fonema):
#     if fonema == 'i' or fonema == 'ɨ' or fonema == 'uj':
#         return 'i'
#     elif fonema == 'e' or fonema == 'ej':
#         return 'e'
#     elif fonema == 'ɛ':
#         return 'ɛ'
#     elif fonema == 'a':
#         return 'a'
#     elif fonema == 'ɐ':
#         return 'ɐ'
#     elif fonema == 'o' or fonema == 'oɦ'or fonema == 'ow' or fonema == 'oj':
#         return 'o'
#     elif fonema == 'ɔ' or fonema == 'ɔw':
#         return 'ɔ'
#     elif fonema == 'u' or fonema == 'uw':
#         return 'u'
#     elif fonema == 'ẽ' or fonema == 'ẽj':
#         return 'ẽ'
#     elif fonema == 'ã' or fonema == 'ɐ̃':
#         return 'ã'
#     elif fonema == 'õ' or fonema == 'ɔ̃':
#         return 'õ'
#     elif fonema == 'ĩ':
#         return 'ĩ'
#     elif fonema == 'ũ' or fonema == 'ũj':
#         return 'ũ'
#     else:
#         return fonema

def tratar_fonemas(row):
    tonica_fonetica_num = row['tonica_fonetica_num']
    divisao_fonetica = row['divisao_fonetica']
    # print(tonica_fonetica_num, divisao_fonetica)

    divisao_fonetica_tratada = []
    for fonema in divisao_fonetica:
        fonema = unicodedata.normalize('NFC', fonema).replace('ɦ', 'h').replace('ɫ', 'w').replace('ɾ', '')
        # ŋ 
        # se for tônica, tirar indicador
        if 'ˈ' in fonema:
            fonema = fonema.split('ˈ')[-1]
            divisao_fonetica_tratada.append('*')

        # verificar a lista de consoantes
        lista_de_consoantes = ['tˌ', 'mw', 'k', 'gwˌ', 'gw', 'spɾ', 'rj', 'ʎˌ', 'lˌ', 'h', 'ɦ', 'blˌ', 'ʒ', 'pˌ', 'pɾ', 't', 'zj', 'zˌ', 'bɾj', 'glj', 'dʒ', 'tʃj', 'kɾˌ', 'ʎ', 'plj', 'sw', 'bɾ', 'vɾ', 'f', 'ɲ', 'ft', 'tsj', 'x', 'gɾˌ', 'bl', 'klj', 'v', 's', 'p', 'z', 'gˌ', 'fj', 'bj', 'kz', 'ɦw', 'kɾw', 'kɾ', 'w', 'fɾ', 'fˌ', 'tʃˌ', 'g', 'gɾ', 'tɾ', 'pj', 'ɾj', 'dɾ', 'gɾw', 'ɾw', 'mˌ', 'fl', 'ng', 'ps', 'kɾj', 'dɾw', 'tɾj', 'vj', 'dw', 'bˌ', 'tɾˌ', 'ks', 'gj', 'pl', 'ʃj', 'sˌ', 'ɦˌ', 'm', 'tʃ', 'blj', 'pɾw', 'dɾj', 'zw', 'l', 'd', 'lj', 'pɾˌ', 'mj', 'sk', 'kl', 'ˌ', 'st', 'kw', 'j', 'ts', 'kˌ', 'nj', 'ms', 'nˌ', 'bw', 'ɦj', 'dˌ', 'r', 'pw', 'fɾˌ', 'ɾ', 'sj', 'ʃ', 'gw', 'tsˌ', 'cr', 'b', 'nw', 'plˌ', 'ɾˌ', 'kj', 'lw', 'pɾj', 'n', 'fɾj', 'vˌ', 'gl', 'tl']
        
        for elem in lista_de_consoantes:
            if fonema.startswith(elem):
                fonema = fonema.replace(elem, '')
                continue
        divisao_fonetica_tratada.append(fonema_simples(tonica_fonetica_num, fonema.replace('ˌ', '').replace('z', '').replace('ʒ', 'j').replace('ʃ', 'j').replace('h', '').replace('k', '').replace('b', '')))
    return divisao_fonetica_tratada