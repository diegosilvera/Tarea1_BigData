from django.shortcuts import render

from words.settings import DATASET_URL
from words_app.models import Procesamiento
from words_app.words import how_many_words, words_in_news, how_many_times, N_most_common_words_in_news


def index(request):
    return render(request, 'index.html')

def literalA(request):
    return  render(request, 'literalA.html')
    
def literalB(request):
    return  render(request, 'literalB.html')

def literalC(request):
    return  render(request, 'literalC.html')

def literalD(request):
    return  render(request, 'literalD.html')

def literalE(request):
    return  render(request, 'literalE.html')

def literalF(request):
    return  render(request, 'procesar.html')

def procesamiento_archivos(request):
    if request.method == 'POST':
        print('solicitud POST', request.POST)
        solicitud = Procesamiento()
        solicitud.archivo = request.POST['archivo']
        solicitud.numero_palabras = request.POST['numero_palabras']

        resultados = []
        resultados.append(reto_a(DATASET_URL+solicitud.archivo))
        #resultados.append(reto_b(DATASET_URL + solicitud.archivo))
        resultados.append(reto_c(DATASET_URL + solicitud.archivo, int(solicitud.numero_palabras)))

        solicitud.resultado = resultados
        solicitud.save()
        print(solicitud)

    return render(request, 'procesar.html',
                  {'solicitud': 'solicitud'})

def reto_a(file):
    total_palabras = how_many_words(file)
    return {"reto_a": total_palabras}

def reto_b(file):
    words=words_in_news(file)
    times=[]
    for wordList in words:
        for word in wordList:
            how_many_t=how_many_times(file,word)
            times.append(word+":"+str(how_many_t))
    return {"reto_b": times}

def reto_c(file, n):
    words=N_most_common_words_in_news(file,n)
    return {"reto_c": words}