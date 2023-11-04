import os
import csv
import Scrapper.scrapper as scrapper

def bfs(letter):
    url = "http://www.portaldalinguaportuguesa.org"
    suffix = "/index.php?action=fonetica&region=rjo&act=list&letter=" + letter
    final = []
    full_link = url+suffix
    final = scrapper.get_entries_page(full_link)
    search = False
    seguinte, search = scrapper.find_seguintes(url, full_link)
    while search:
        final.extend(scrapper.get_entries_page(seguinte))
        seguinte, search = scrapper.find_seguintes(url, seguinte)
    print(final[0])

    fields = ['palavra', 'categoria', 'divisao_silabica', 'tonica_silabica', 'tonica_silabica_num', 'divisao_fonetica', 'tonica_fonetica', 'tonica_fonetica_num', 'antepenultima_fonetica', 'penultima_fonetica', 'ultima_fonetica']

    with open("./labeled/" + letter + ".csv", 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(final)

# uma pasta para cada projeto
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory) 