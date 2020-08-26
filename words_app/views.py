from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,JsonResponse
from .models import News
from .funcs import how_many_words
import requests

def index(request):
    literal_list=['literalA','literalB','literalC','literalD','literalE','literalF']
    context={'literal_list':literal_list}
    return render(request, 'index.html',context)

def literalA(request):
    return  render(request, 'literalA.html')
    
def literalB(request):
    return  render(request, 'literalB.html')

def literalC(request):
    news_list=News.objects.all()
    context={'news_list':news_list}
    return  render(request, 'literalC.html',context)

def literalD(request):
    try:
        selected_choice=News.objects.all().get(pk=request.POST['Noticias'])
    except(KeyError,News.DoesNotExist):
        return render(request,'literalC.html',{'error_message': "No seleccionate un archivo."})
    else: 
        
        return HttpResponse('Hay '+str(how_many_words(selected_choice.news_id))+" palabras en "+str(selected_choice.news_id))


def literalE(request):
    return  render(request, 'literalE.html')

def literalF(request):
    return  render(request, 'literalF.html')
