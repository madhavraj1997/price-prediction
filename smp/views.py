from multiprocessing import context
from django.shortcuts import render


# Create your views here.
def home(request):
    context={}
    return render(request, 'code/home.html', context)

def portfolio(request):
    context={}
    return render(request, 'code/portfolio.html', context)

def price_prediction(request):
    context = {}
    return render(request, 'code/price_prediction.html', context)

def watchlist(request):
    context = {}
    return render(request, 'code/watchlist.html', {})
