def fonema_num(fonema):
    # lista_de_consoantes = ['tˌ', 'mw', 'k', 'gwˌ', 'spɾ', 'rj', 'ʎˌ', 'lˌ', 'ɦ', 'blˌ', 'pˌ', 'pɾ', 't', 'zj', 'zˌ', 'bɾj', 'glj', 'tʃj', 'kɾˌ', 'ʎ', 'plj', 'sw', 'bɾ', 'vɾ', 'f', 'ɲ', 'ft', 'tsj', 'x', 'gɾˌ', 'bl', 'klj', 'v', 's', 'p', 'z', 'gˌ', 'fj', 'bj', 'kz', 'ɦw', 'kɾw', 'kɾ', 'fɾ', 'fˌ', 'tʃˌ', 'g', 'gɾ', 'tɾ', 'pj', 'ɾj', 'dɾ', 'gɾw', 'ɾw', 'mˌ', 'fl', 'ng', 'ps', 'kɾj', 'dɾw', 'tɾj', 'vj', 'dw', 'bˌ', 'tɾˌ', 'ks', 'gj', 'pl', 'ʃj', 'sˌ', 'ɦˌ', 'm', 'tʃ', 'blj', 'pɾw', 'dɾj', 'zw', 'l', 'd', 'lj', 'pɾˌ', 'mj', 'sk', 'kl', 'ˌ', 'st', 'kw', 'ts', 'kˌ', 'nj', 'ms', 'nˌ', 'bw', 'ɦj', 'dˌ', 'r', 'pw', 'fɾˌ', 'ɾ', 'sj', 'ʃ', 'gw', 'tsˌ', 'cr', 'b', 'nw', 'plˌ', 'ɾˌ', 'kj', 'lw', 'pɾj', 'n', 'fɾj', 'vˌ', 'gl', 'tl']
    # for elem in lista_de_consoantes:
    #     if fonema.endswith(elem):
    #         fonema = fonema.replace(elem, '')
    #         continue
    if fonema == 'i' or fonema == 'ɨ' or fonema == 'uj':
        return 1
    elif fonema == 'e' or fonema == 'ej':
        return 2
    elif fonema == 'ɛ':
        return 3
    elif fonema == 'a':
        return 4
    elif fonema == 'ɐ':
        return 5
    elif fonema == 'o' or fonema == 'oɦ'or fonema == 'ow' or fonema == 'oj':
        return 6
    elif fonema == 'ɔ' or fonema == 'ɔw':
        return 7
    elif fonema == 'u' or fonema == 'uw':
        return 8
    elif fonema == 'ẽ' or fonema == 'ẽj':
        return 9
    elif fonema == 'ã' or fonema == 'ɐ̃':
        return 10
    elif fonema == 'õ' or fonema == 'ɔ̃':
        return 11
    elif fonema == 'ĩ':
        return 12
    elif fonema == 'ũ' or fonema == 'ũj':
        return 13
    elif fonema == 'ɐ̃j':
        return 14
    elif fonema == 'aw':
        return 15
    elif fonema == 'ew':
        return 16
    elif fonema == 'ɛw':
        return 17
    elif fonema == 'iw':
        return 18
    elif fonema == 'aj':
        return 19
    elif fonema == 'ɛj':
        return 20
    elif fonema == 'ɔj':
        return 21
    elif fonema == 'ɐ̃w':
        return 22
    elif fonema == 'õj':
        return 23
    elif fonema == 'ẽj':
        return 24
    elif fonema == 'ʊ':
        return 25
    elif fonema == 'ɪ':
        return 26
    else:
        return -1
    
