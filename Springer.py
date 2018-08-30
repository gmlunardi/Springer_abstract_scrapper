# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 21:02:37 2018

@author: Gabriel


"""

import bibtexparser
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.0 Safari/537.36'}


with open('search_Springer.bib', encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
    
ordem = 1
for entry in bib_database.entries:
    print(entry['ID'])
    url = entry['url']
    print(url)
    if 'abstract' not in entry:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        soup.encode("utf-8")
        abstract = soup.find('section', {'class':'Abstract'})
        if abstract is None:
            print('não encontrou nada, parando agora! Verifique a URL, a conexão, a tag ou, então, se o IP não foi bloqueado!')
            break
        else:
            print(ordem)
            ordem += 1
            print('abstract coletado')
            print('\n')
            entry['abstract'] = abstract.text
    
    
with open('search_Springer.bib', 'w', encoding="utf-8") as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)
    