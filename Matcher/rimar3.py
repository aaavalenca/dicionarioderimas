import os
import pandas as pd

def tarara(df):
    vogais = {'a' : ['a', 'á', 'ã', 'â'],
            'e' : ['e', 'é', 'ê'],
            'i' : ['i', 'í'],
            'o' : ['o', 'ó', 'ô', 'õ'],
            'u' : ['u', 'ú']}

    tarara = []

    for index, word in df.iterrows():
        isTarara = True
        vogal = []
        for i, silaba in enumerate(word['divisao_silabica']):
            if i == 0:
                for key, values in vogais.items():
                    if any(val in silaba for val in values):
                        vogal = values
            else:
                if any(v in silaba for v in vogal):
                    continue
                else:
                    isTarara = False
                    break
        if isTarara:
            tarara.append(word)

    return tarara

def ler_repetidas():
    vogais: {
        'a' : ['a', 'á', 'ã'],
        'e' : ['e', 'é', 'ê'],
        'i' : ['i', 'í'],
        'o' : ['o', 'ó', 'ô', 'õ'],
        'u' : ['u', 'ú'],
    }
    pd.set_option('display.max_rows', None)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(current_directory, '..', 'Scrapper/PortalLP/DB/Completo', 'database.csv')
    df = pd.read_csv(relative_path, converters={'divisao_silabica' : eval, 'tonica_silabica_num' : int, 'divisao_fonetica' : eval, 'tonica_fonetica_num' : int})
    df = (df[df['divisao_silabica'].apply(lambda x: len(x) > 2)])
    selected_rows = tarara(df)
    selected_df = pd.DataFrame(selected_rows)
    print(selected_df['palavra'])


ler_repetidas()