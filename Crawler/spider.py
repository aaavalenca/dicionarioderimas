import link_finder
import urllib.robotparser as urlrobot
import urllib.request as rq
import os
import csv

def bfs(letter):
    url = "http://www.portaldalinguaportuguesa.org"
    suffix = "/index.php?action=fonetica&region=rjo&act=list&letter=" + letter
    final = []
    full_link = url+suffix

    # rp = urlrobot.RobotFileParser()
    # rp.set_url(url + "/robots.txt")
    # rp.read()
    # rp.crawl_delay("3")
    # if rp.can_fetch("*", url + suffix):

    # create_project_dir(folder)
    final = link_finder.get_entries_page(full_link)
    search = False
    seguinte, search = link_finder.find_seguintes(url, full_link)
    while search:
        final.extend(link_finder.get_entries_page(seguinte))
        seguinte, search = link_finder.find_seguintes(url, seguinte)
    print(final[0])

    fields = ['palavra', 'divisao', 'categoria', 'fonetica', 'tonic']

    with open("rimas/" + letter + ".csv", 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(final)

# uma pasta para cada projeto
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# def create_data_files(project_name, base_url):
    # if not os.path.isfile(crawled):
    #     write_file(crawled, '')

# def write_file(path, data):
#     f = open(path, 'w')
#     f.write(data)
#     f.close()

# def append_to_file(path, data):
#     with open(path, 'a') as file:
#         file.write(data + '\n')

# # deletar o conteúdo de um arquivo
# def delete_file_contents(path):
#     with open(path, 'w'):
#         pass

# # converter urls para itens de um set (readtextfile)
# def file_to_set(filename):
#     results = set()
#     with open(filename, 'rt') as f:
#         for line in f:
#             results.add(line.replace('\n', ''))
#     return results

# # pegar os itens do set e colocar como linhas de texto noutro arquivo
# def set_to_file(links, file):
#     delete_file_contents(file)
#     for link in sorted(links):
#         append_to_file(file, link)

# def heuristic_set_to_file(links, file):
#     delete_file_contents(file)
#     for link in links:
#         append_to_file(file, link[1])

# def save_html(base_url, page, count):
#     crawled = base_url + "/" + str(count) + ".html"
#     write_file(crawled, page)        