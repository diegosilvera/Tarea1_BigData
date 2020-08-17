# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 08:46:46 2020

@author: Dell Inspiron14-3443
"""
from bs4 import BeautifulSoup
import urllib.request
import tarfile as tf
import re
from collections import Counter
from itertools import chain
import numpy as np
tfstream=urllib.request.urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/reuters21578-mld/reuters21578.tar.gz')
reuters=tf.open(fileobj=tfstream,mode='r:gz')
reuters.extractall()
reuters.close()

#a. Cuenta el número de palabras en un archivo, dado el nombre del archivo. Por defecto, escogimos reut2-002.sgm
# param id_file el nombre del archivo escogido.
def how_many_words(id_file='reut2-002.sgm'):
    soup=BeautifulSoup(open(id_file),'html.parser')
    ocurrences=soup.find_all('body')
    how_many=0
    for item in ocurrences:
        lines=item.get_text()
        how_many+=len(re.split('[\n ]+',lines))-2
    return how_many

#b. Cuenta el número de veces que cierta palabra aparece en un archivo, con el nombre del archivo pasado por parámetro
# param id_file el nombre del archivo escogido
# param word La palabra para la cual se hace el conteo.
def how_many_times(id_file='reut2-002.sgm',word):

    soup=BeautifulSoup(open(id_file),'html.parser')
    ocurrences=soup.find_all('body',string=re.compile(word))
    how_many=0
    for item in ocurrences:
        lines=item.get_text()
        how_many+=lines.count(word)
    return how_many

# Retorna la lista de palabras en un archivo dado su nombre
# param id_file el nombre del archivo escogido
def words_in_news(id_file):
    soup=BeautifulSoup(open(id_file),'html.parser')
    ocurrences=soup.find_all('body')
    words=[]
    for item in ocurrences:
        lines=item.get_text()
        words.append(re.split('[\n ]+',lines)[:-2]) 
    return words

#c y d. Retorna las N palabras más comúnes en un archivo. Por defecto se pasa reut-002.sgm
# param id_file el nombre del archivo escogido
# param N el número de palabras
def N_most_common_words_in_news(id_file='reut2-002.sgm', N):
    words=words_in_news(id_file)
    counter=Counter(chain.from_iterable(words))
    return counter.most_common(N)

# e. Retorna una tupla de dos elementos donde cada uno de los elementos es una lista con las N palabras más repetidas en dos archivos.
# param id_file_1 el nombre de uno de los dos archivos
# param id_file_2 el nombre del segundo archivo
# param N el número de palabras
def N_most_common_words_in_news_two(id_file_1,id_file_2,N):
    return N_most_common_in_news(id_file_1,N),N_most_common_in_news(id_file_2,N)

# f. Retorna una lista con una cierta cantidad de elementos donde cada elemento es una lista que está en biyección con cada archivo en una lista X de archivos
# param X lista con nombres de archivos
# param N el número de palabras
def N_most_common_words_in_news_X(X, N):
    N_most_common=[]
    for id_file in X:
        N_most_common.append(N_most_common__words_in_news(id_file,N))
    return N_most_commo

# g. Retorna una tupla de dos elementos, donde el primero de estos corresponde al nombre del archivo en una lista de X archivos en el que aparece más veces cierta palabra,
#    y el segundo elemento dice cuál archivo tiene más palabras.
# param X lista con nombres de archivos
# param word la palabra escogida
def which_file_has_more_ocurrences(X,word):
    words_ocurrences=[]
    lengths=[]
    for id_file in X:
        length=how_many_words(id_file)
        times=how_many_times(id_file,word)
        lengths.append(length)
        words_ocurrences.append(times)
        
    words_ocurrences=np.array(words_ocurrences)
    lengths=np.array(lengths)
    return X[np.argmax(words_ocurrences)],X[np.argmax(lengths)]