import re
from collections import Counter
from itertools import chain

from bs4 import BeautifulSoup


# Cuenta el número de palabras en un archivo, dado el nombre del archivo
# param id_file el nombre del archivo escogido
def how_many_words(id_file):
    soup = BeautifulSoup(open(id_file), 'html.parser')
    ocurrences = soup.find_all('body')
    how_many = 0
    for item in ocurrences:
        lines = item.get_text()
        how_many += len(re.split('[\n ]+', lines)) - 2
    return how_many


# Cuenta el número de veces que cierta palabra aparece en un archivo
# param id_file el nombre del archivo escogido
# param word La palabra para la cual se hace el conteo
def how_many_times(id_file, word):
    soup = BeautifulSoup(open(id_file), 'html.parser')
    ocurrences = soup.find_all('body', string=re.compile(word))
    how_many = 0
    for item in ocurrences:
        lines = item.get_text()
        how_many += lines.count(word)
    return how_many


# Retorna la lista de palabras en un archivo dado su nombre
# param id_file el nombre del archivo escogido
def words_in_news(id_file):
    soup = BeautifulSoup(open(id_file), 'html.parser')
    ocurrences = soup.find_all('body')
    words = []
    for item in ocurrences:
        lines = item.get_text()
        words.append(re.split('[\n ]+', lines)[:-2])
    return words


# Retorna las N palabras más comúnes en un archivo
# param id_file el nombre del archivo escogido
# param N el número de palabras
def N_most_common_words_in_news(id_file, N):
    words = words_in_news(id_file)
    counter = Counter(chain.from_iterable(words))
    return counter.most_common(N)
