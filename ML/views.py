from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    return render(request, 'index.html')

def classification(request):
    return render(request, 'classification.html')

def regression(request):
    return render(request, 'regression.html')


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
