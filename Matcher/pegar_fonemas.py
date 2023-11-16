import pandas as pd
import re
import os

def pegar_fonemas():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join(current_directory, '..', 'Scrapper/PortalLP/DB/Completo', 'database.csv')
    df = pd.read_csv(relative_path, converters={'divisao_silabica' : eval, 'tonica_silabica_num' : int, 'divisao_fonetica' : eval, 'tonica_fonetica_num' : int})
    
    unique_phonemes = list(set(item for sublist in [x for x in df['divisao_fonetica']] for item in sublist))
    print(unique_phonemes)
    print("___________")
    unique_chars = list(set(item.lower() for sublist in [x for x in df['palavra']] for item in sublist))
    print(unique_chars)

pegar_fonemas()