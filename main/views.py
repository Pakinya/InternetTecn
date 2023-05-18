from django.shortcuts import render
from .models import Artiles
from .models import Goroskop

def mainpage(request):
    return render(request, 'main/mainpage.html')

def goroskop(request):
    goroskop = Goroskop.objects.all()
    return render(request, 'main/goroskop.html', {'goroskop': goroskop})

def result(request):
    return render(request, 'main/result.html')


def news(request):
    newsS = Artiles.objects.all()
    return render(request, 'main/news.html', {'newsS': newsS})