import pandas as pd
import os

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