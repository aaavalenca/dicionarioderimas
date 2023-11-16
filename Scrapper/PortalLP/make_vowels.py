import pandas as pd
import unicodedata

def fonema_simple(fonema):
    if fonema == 'i' or fonema == 'ɨ' or fonema == 'uj':
        return 'i'
    elif fonema == 'e' or fonema == 'ej':
        return 'e'
    elif fonema == 'ɛ':
        return 'ɛ'
    elif fonema == 'a':
        return 'a'
    elif fonema == 'ɐ':
        return 'ɐ'
    elif fonema == 'o' or fonema == 'oɦ'or fonema == 'ow' or fonema == 'oj':
        return 'o'
    elif fonema == 'ɔ' or fonema == 'ɔw':
        return 'ɔ'
    elif fonema == 'u' or fonema == 'uw':
        return 'u'
    elif fonema == 'ẽ' or fonema == 'ẽj':
        return 'ẽ'
    elif fonema == 'ã' or fonema == 'ɐ̃':
        return 'ã'
    elif fonema == 'õ' or fonema == 'ɔ̃':
        return 'õ'
    elif fonema == 'ĩ':
        return 'ĩ'
    elif fonema == 'ũ' or fonema == 'ũj':
        return 'ũ'
    else:
        return fonema

def tratar_fonemas(divisao_fonetica):
    divisao_fonetica_tratada = []
    for fonema in divisao_fonetica:
        fonema = unicodedata.normalize('NFC', fonema).replace('ɦ', 'h')
        # se for tônica, tirar indicador
        if 'ˈ' in fonema:
            fonema = fonema.split('ˈ')[-1]
            divisao_fonetica_tratada.append('*')

        # verificar a lista de consoantes
        lista_de_consoantes = ['tˌ', 'mw', 'k', 'gwˌ', 'spɾ', 'rj', 'ʎˌ', 'lˌ', 'h', 'ɦ', 'blˌ', 'pˌ', 'pɾ', 't', 'zj', 'zˌ', 'bɾj', 'glj', 'tʃj', 'kɾˌ', 'ʎ', 'plj', 'sw', 'bɾ', 'vɾ', 'f', 'ɲ', 'ft', 'tsj', 'x', 'gɾˌ', 'bl', 'klj', 'v', 's', 'p', 'z', 'gˌ', 'fj', 'bj', 'kz', 'ɦw', 'kɾw', 'kɾ', 'w', 'fɾ', 'fˌ', 'tʃˌ', 'g', 'gɾ', 'tɾ', 'pj', 'ɾj', 'dɾ', 'gɾw', 'ɾw', 'mˌ', 'fl', 'ng', 'ps', 'kɾj', 'dɾw', 'tɾj', 'vj', 'dw', 'bˌ', 'tɾˌ', 'ks', 'gj', 'pl', 'ʃj', 'sˌ', 'ɦˌ', 'm', 'tʃ', 'blj', 'pɾw', 'dɾj', 'zw', 'l', 'd', 'lj', 'pɾˌ', 'mj', 'sk', 'kl', 'ˌ', 'st', 'kw', 'j', 'ts', 'kˌ', 'nj', 'ms', 'nˌ', 'bw', 'ɦj', 'dˌ', 'r', 'pw', 'fɾˌ', 'ɾ', 'sj', 'ʃ', 'gw', 'tsˌ', 'cr', 'b', 'nw', 'plˌ', 'ɾˌ', 'kj', 'lw', 'pɾj', 'n', 'fɾj', 'vˌ', 'gl', 'tl']
        
        for elem in lista_de_consoantes:
            if fonema.startswith(elem):
                fonema = fonema.replace(elem, '')
                continue
        divisao_fonetica_tratada.append(fonema_simple(fonema))
    return divisao_fonetica_tratada