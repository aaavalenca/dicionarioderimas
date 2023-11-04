import requests
from bs4 import BeautifulSoup
import re
import os
import csv
from multiprocessing import Pool
import PortalLP.manipulate_database as md

letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ] 

def check_word(word):
    pattern = "^[a-z-]*$"
    not_in_database = md.not_in_database(word)
    real_word = bool(re.match(pattern, word))
    sizeable = len(word) > 2
    return not_in_database and real_word and sizeable and word 

def get_informal_words(link):
    website_url = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(website_url,'html.parser')
    div = soup.find_all(class_="card-body card-padding")
    words = []
    for href in div[0].find_all('a', href=True):
        word = href['title'].replace("Significado de ", "").lower()
        word = re.split(r"[ ,-]", word)[-1]
        if check_word(word):
            words.append(word)
    return words, soup

def find_proxima(soup):
    a_tags = soup.findAll('a', attrs={"aria-label": True})
    for at in a_tags:
        if at['aria-label'] == "Próxima":
            print(at['href'])
            return at['href'], True
    return "", False

def bfs(letter):
    url = "https://www.dicionarioinformal.com.br"
    suffix = "/letra/" + letter + "/1"
    full_link = url + suffix
    final, soup = get_informal_words(full_link)
    append_to_file('Data/novas/' + letter + '.csv', final)
    search = False
    proxima, search = find_proxima(soup)
    while search:
        f, s = get_informal_words(url+proxima)
        append_to_file('Data/novas/' + letter + '.csv', f)
        final.extend(f)
        proxima, search = find_proxima(s)
    return final

def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def append_to_file(filename, new):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        content = list(reader)[1]
        content.extend(new)
    with open(filename, 'w') as f:
        write = csv.writer(f)
        write.writerow(["palavra"])
        write.writerows([content])
        f.close()

def new_words(letter):
    print("Starting..." + letter)
    create_project_dir('Data/novas')
    fields = ['palavra']
    with open('Data/novas/' + letter + '.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows([[letter]]) 
    all_new_words = bfs(letter)
    print(all_new_words)

def main():
    letters = ['a', 'c', 'p']
    pool = Pool(len(letters))
    pool.map(new_words,letters)
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()