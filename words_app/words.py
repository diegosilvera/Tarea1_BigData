# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 08:46:46 2020

@author: Dell Inspiron14-3443
"""
from bs4 import BeautifulSoup
import urllib.request
import tarfile as tf
import re,os
from collections import Counter
from itertools import chain
import numpy as np
PATH="../Resultados/"
if not os.path.exists(os.path.dirname(PATH)):
    os.makedirs(os.path.dirname(PATH))

#tfstream=urllib.request.urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/reuters21578-mld/reuters21578.tar.gz')
#reuters=tf.open(fileobj=tfstream,mode='r:gz')
reuters=tf.open("reuters21578.tar.gz",mode='r:gz')
reuters.extractall()
reuters.close()

#a. Cuenta el número de palabras en un archivo, dado el nombre del archivo. Por defecto, escogimos reut2-002.sgm
# param id_file el nombre del archivo escogido.
def how_many_words(id_file):
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
def how_many_times(id_file, word):

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
def N_most_common_words_in_news(id_file, N):
    words=words_in_news(id_file)
    counter=Counter(chain.from_iterable(words))
    return counter.most_common(N)

#----------------------------------------------------------------------------------------------------------------------
#Exportando respuesta reto a
print("Procesando reto a...")
how_many_w=how_many_words('reut2-002.sgm')
print("Exportando resultados del reto a")
fileRetoA = open(PATH+"resultados_reto_A.txt","w")
fileRetoA.write("El archivo reut2-002.sgm tiene "+str(how_many_w)+" palabras")
fileRetoA.close()

#Exportando respuesta reto b
def reto_b(id_file):
    words=words_in_news(id_file)
    times=[]
    for wordList in words:
        for word in wordList:
            how_many_t=how_many_times(id_file,word)
            times.append(word+":"+str(how_many_t))
    return times

print("Procesando reto b...")
#times=reto_b('reut2-002.sgm')
print("Exportando resultados del reto b")
fileRetoB = open(PATH+"resultados_reto_B.txt","w")
#for frase in times:
    #fileRetoB.write(frase)
fileRetoB.close()

#Exportando respuesta reto c
print("Digite el numero de palabras:")
N=input()
print("Procesando reto c...")
words=N_most_common_words_in_news('reut2-002.sgm',int(N))
print("Exportando resultados del reto c")
fileRetoC = open(PATH+"resultados_reto_C.txt","w")
for pair in words:
    fileRetoC.write(pair[0]+"\n")
fileRetoC.close()

#Exportando respuesta reto d
print("Digite el numero de palabras:")
N=input()
print("Digite nombre del archivo:")
id_file=input()
print("Procesando reto d...")
words=N_most_common_words_in_news(id_file,int(N))
print("Exportando resultados del reto d")
fileRetoD = open(PATH+"resultados_reto_D.txt","w")
for w in words:
    fileRetoD.write(w[0]+"\n")
fileRetoD.close()

#---------------------------------------------E:EXPORTANDO ARCHIVOS DE RETOS A-D CON 2 ARCHIVOS---------------------------- 
print("------------E:EXPORTANDO ARCHIVOS DE RETOS A-D CON 2 ARCHIVOS----------------")
#Exportando respuesta reto a
print("Procesando reto E-A...")
how_many_w=how_many_words('reut2-002.sgm')+how_many_words('reut2-013.sgm')
print("Exportando resultados del reto E-A")

#Exportando respuesta reto b
print("Procesando reto E-B...")
#times=reto_b('reut2-002.sgm')+reto_b('reut2-013.sgm')
print("Exportando resultados del reto E-B")

#Exportando respuesta reto c
print("Digite el numero de palabras:")
N=input()
print("Procesando reto E-C...")
words=N_most_common_words_in_news('reut2-002.sgm',int(N))+N_most_common_words_in_news('reut2-013.sgm',int(N))
print("Exportando resultados del reto E-C")

#Exportando respuesta reto d
print("Digite el numero de palabras:")
N=input()
print("Digite nombre del primer archivo:")
id_file=input()
print("Digite nombre del segundo archivo:")
id_file2=input()
print("Procesando reto E-D...")
words=N_most_common_words_in_news(id_file,N)+N_most_common_words_in_news(id_file2,N)
print("Exportando resultados del reto E-D")
#---------------------------------------------F:EXPORTANDO ARCHIVOS DE RETOS A-D CON X ARCHIVOS---------------------------- 
print("------------F:EXPORTANDO ARCHIVOS DE RETOS A-D CON X ARCHIVOS----------------")
print("Digite el numero de archivos: ")
X=input()
files_array=[]
for i in range(0,int(X)):
    print("Digite nombre del archivo #"+str(i+1))
    files_array.append(input())
#Exportando respuesta reto a
print("Procesando reto F-A...")
for f in files_array:
    how_many_w+=how_many_words(f)
print("Exportando resultados del reto F-A")

#Exportando respuesta reto b
print("Procesando reto F-B...")
#for f in files_array:
 #   times+=reto_b(f)
print("Exportando resultados del reto F-B")

#Exportando respuesta reto c y d
print("Digite el numero de palabras:")
N=input()
print("Procesando reto F-C y D...")
for f in files_array:
    words+=N_most_common_words_in_news(f,int(N))
print("Exportando resultados del reto F-C y D")
#--------------------------------------------------------------G---------------------------------------------------------
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


print("------------G----------------")
print("Digite el numero de archivos: ")
X=input()
files_array=[]
for i in range(0,int(X)):
    print("Digite nombre del archivo #"+str(i+1))
    files_array.append(input())
print("Digite la palabra: ")
word=input()
print("Procesando reto G...")
resultado=which_file_has_more_ocurrences(files_array,word)
print("Exportando resultados del reto G")
fileRetoG = open(PATH+"resultados_reto_G.txt","w")
#####TODO revisar
fileRetoG.write(resultado)
fileRetoG.close()

print("------------H----------------")
# Estructura del comando UNIX: python words.py <archivo1> <num_palabras_archivo1> <archivo2> <num_palabras_archivo2 <archivo3> <num_palabras_archivo3>
# Inicia proceso primer archivo
words_primer_proceso = N_most_common_words_in_news(sys.argv[1],int(sys.argv[2]))
print("Exportando resultados del primer proceso")
fileRetoH1 = open(PATH+"resultados_reto_H_archivo1.txt","w")
for w in words_primer_proceso:
    fileRetoH1.write(w[0]+"\n")
fileRetoH1.close()
# Inicia proceso segundo archivo
words_segundo_proceso = N_most_common_words_in_news(sys.argv[3],int(sys.argv[4]))
print("Exportando resultados del segundo proceso")
fileRetoH2 = open(PATH+"resultados_reto_H_archivo2.txt","w")
for w in words_segundo_proceso:
    fileRetoH2.write(w[0]+"\n")
fileRetoH2.close()
# Inicia proceso tercer archivo
words_tercer_proceso = N_most_common_words_in_news(sys.argv[5],int(sys.argv[6]))
print("Exportando resultados del tercer proceso")
fileRetoH3 = open(PATH+"resultados_reto_H_archivo3.txt","w")
for w in words_tercer_proceso:
    fileRetoH3.write(w[0]+"\n")
fileRetoH3.close()

print("Finaliza reto H")

print("------------I----------------")
# Al pasar los demas procesos a la estructura django deberia quedar solo el punto h en este script
# El siguiente comando ejecuta el script cada domingo a las 8:00am utilizando crontab
# 0 8 * * 0 /Tarea1_BigData python words.py reut2-000.sgm 2 reut2-004.sgm 1 reut2-006.sgm 4
