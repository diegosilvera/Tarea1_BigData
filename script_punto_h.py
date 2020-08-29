import sys

from words.settings import DATASET_URL, RESULTADOS_URL
from words_app.words import N_most_common_words_in_news

# Estructura del comando UNIX: python script_punto_h.py <archivo1> <num_palabras_archivo1> <archivo2> <num_palabras_archivo2 <archivo3> <num_palabras_archivo3>
# Inicia proceso primer archivo
words_primer_proceso = N_most_common_words_in_news(DATASET_URL+sys.argv[1],int(sys.argv[2]))
print("Exportando resultados primer archivo ")
fileRetoH1 = open(RESULTADOS_URL+"resultados_reto_H_archivo1.txt","w")
for w in words_primer_proceso:
    fileRetoH1.write(w[0]+"\n")
fileRetoH1.close()
# Inicia proceso segundo archivo
words_segundo_proceso = N_most_common_words_in_news(DATASET_URL+sys.argv[3],int(sys.argv[4]))
print("Exportando resultados segundo archivo")
fileRetoH2 = open(RESULTADOS_URL+"resultados_reto_H_archivo2.txt","w")
for w in words_segundo_proceso:
    fileRetoH2.write(w[0]+"\n")
fileRetoH2.close()
# Inicia proceso tercer archivo
words_tercer_proceso = N_most_common_words_in_news(DATASET_URL+sys.argv[5],int(sys.argv[6]))
print("Exportando resultados tercer archivo")
fileRetoH3 = open(RESULTADOS_URL+"resultados_reto_H_archivo3.txt","w")
for w in words_tercer_proceso:
    fileRetoH3.write(w[0]+"\n")
fileRetoH3.close()
print("Finaliza proceso")