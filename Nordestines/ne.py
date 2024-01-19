from PyPDF2 import PdfReader
import os
import csv


script_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_path)
pdf_path = "dicionario_ne.pdf"
reader = PdfReader(pdf_path)
number_of_pages = len(reader.pages)
page = reader.pages

dict_ne = {}

def split_words(t):
    return t.split('\n')

for page_num in range(len(reader.pages)):
    text = page[page_num].extract_text()
    pairs = split_words(text)
    
    for pair in pairs:
        separated = pair.split(' - ')
        if len(separated) > 1:
            dict_ne[separated[0]] = separated[1]

print(dict_ne["BUNEQUEIRO"])

csv_file_path = 'dicionario_ne.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Key', 'Value'])
    for key, value in dict_ne.items():
        csv_writer.writerow([key, value])