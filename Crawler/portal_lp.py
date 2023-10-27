import scrapper
# import urllib.robotparser as urlrobot
# import urllib.request as rq
import os
import csv

def bfs(letter):
    url = "http://www.portaldalinguaportuguesa.org"
    suffix = "/index.php?action=fonetica&region=rjo&act=list&letter=" + letter
    final = []
    full_link = url+suffix

    # create_project_dir(folder)
    final = scrapper.get_entries_page(full_link)
    search = False
    seguinte, search = scrapper.find_seguintes(url, full_link)
    while search:
        final.extend(scrapper.get_entries_page(seguinte))
        seguinte, search = scrapper.find_seguintes(url, seguinte)
    print(final[0])

    fields = ['palavra', 'divisao_list', 'divisao', 'categoria', 'fonetica_list', 'fonetica', 'tonica_num', 'tonica', 'antepenultima', 'penultima', 'ultima']

    with open("Crawler/labeled/" + letter + ".csv", 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(final)

# uma pasta para cada projeto
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)