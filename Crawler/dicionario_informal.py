import link_finder2
import urllib.robotparser as urlrobot
import urllib.request as rq
import os
import csv

def bfs(letter):
    url = "https://www.dicionarioinformal.com.br/letra/"
    suffix = letter
    final = []
    full_link = url+suffix

    # create_project_dir(folder)
    final = link_finder2.get_entries_page(full_link)
    search = False
    next, search = link_finder2.find_seguintes(url, full_link)
    while search:
        final.extend(link_finder2.get_entries_page(next))
        next, search = link_finder2.find_seguintes(url, next)
    print(final[0])

    fields = ['palavra']

    with open("informal/" + letter + ".csv", 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(final)

# uma pasta para cada projeto
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)