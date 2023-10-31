import pandas as pd
import os

def clean(df):
    df = df.drop_duplicates(subset=['palavra'])
    return df[(df["palavra"]).str.len() > 2]

def not_in_database(word):
    df = pd.read_csv("Crawler/database/database.csv", delimiter= ",")
    return not ((df['palavra'].eq(word)).any())

def merge_database():
    list_dir = sorted(os.listdir("Crawler/labeled"))
    df = pd.DataFrame()
    for filename in list_dir:
        ndf = pd.read_csv("Crawler/labeled/" + filename, delimiter= ",")
        df = pd.concat([df, clean(ndf)], axis=0, ignore_index=True)
    os.makedirs('Crawler/database', exist_ok=True) 
    df.to_csv("Crawler/database/database.csv")

merge_database()