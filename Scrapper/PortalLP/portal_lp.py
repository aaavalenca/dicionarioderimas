import csv
import scrapper

def bfs(letter):
    url = "http://www.portaldalinguaportuguesa.org"
    sufixo = "/index.php?action=fonetica&region=rjo&act=list&letter=" + letter
    final = []
    link_completo = url+sufixo
    final = scrapper.palavras_da_pagina(link_completo)
    procurar = False
    seguinte, procurar = scrapper.encontrar_seguintes(url, link_completo)
    while procurar:
        final.extend(scrapper.palavras_da_pagina(seguinte))
        seguinte, procurar = scrapper.encontrar_seguintes(url, seguinte)
    print(final)

    campos = ['palavra', 'categoria', 'divisao_silabica', 'tonica_silabica_num', 'divisao_fonetica', 'tonica_fonetica_num']

    with open('Scrapper/PortalLP/DB/Letras/' + letter + '.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(campos)
        write.writerows(final)