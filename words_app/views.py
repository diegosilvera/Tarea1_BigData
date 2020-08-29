from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests

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
    return  render(request, 'literalF.html')
