import pandas as pd
import os
import make_vowels

def clean(df):
    df = df[df["tonica_fonetica_num"] != 0]
    df = df.drop_duplicates(subset=['palavra'])
    return df[(df["palavra"]).str.len() > 2]

def not_in_database(word):
    df = pd.read_csv("Scrapper/PortalLP/DB/Letras/database.csv", delimiter= ",")
    return not ((df['palavra'].eq(word)).any())

def merge_database():
    list_dir = sorted(os.listdir("Scrapper/PortalLP/DB/Letras"))
    df = pd.DataFrame()
    for filename in list_dir:
        print(filename)
        ndf = pd.read_csv("Scrapper/PortalLP/DB/Letras/" + filename, delimiter= ",")
        df = pd.concat([df, clean(ndf)], axis=0, ignore_index=True)
    os.makedirs('Scrapper/PortalLP/DB/Completo', exist_ok=True) 
    df.to_csv("Scrapper/PortalLP/DB/Completo/database.csv")

def make_vowels_only():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(current_directory, '..', 'PortalLP/DB/Completo', 'database.csv')
    df = pd.read_csv(relative_path, converters={'divisao_silabica' : eval, 'tonica_silabica_num' : int, 'divisao_fonetica' : eval, 'tonica_fonetica_num' : int})
    df['divisao_fonetica_simples'] = df['divisao_fonetica'].apply(make_vowels.tratar_fonemas)
    print(df[['palavra','divisao_fonetica_simples']])
        
    os.makedirs('Scrapper/PortalLP/DB/Completo', exist_ok=True) 
    df.to_csv("Scrapper/PortalLP/DB/Completo/database_simple.csv")

make_vowels_only()