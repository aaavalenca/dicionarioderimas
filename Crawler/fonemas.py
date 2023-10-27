def fonema_num(fonema, local):
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
    elif fonema == 'o' or fonema == 'ow' or fonema == 'oj':
        return 6
    elif fonema == 'ɔ' or fonema == 'ɔw':
        return 7
    elif fonema == 'u' or fonema == 'uw':
        return 8
    elif fonema == 'ẽ':
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