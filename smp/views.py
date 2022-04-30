
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Watchlist
from smp.livedata import stocks
from smp.company_name import stock_name
import numpy as np
import pandas as pd
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # model = Item
    

    # csv_working
    #df = pd.read_csv('smp/csv/todaysstock.csv') 
    df = stocks()
    
    print(df)


# loginpage
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'you are successfully loged in.')
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
        

    return render(request, 'code/home.html', {'stocks': df})
    
@login_required
def portfolio(request):
    portfolios = Portfolio.objects.all()
    df = stocks()
    print(type(df))
    context={'portfolios': portfolios, 'df': df}
    return render(request, 'code/portfolio.html', context)
@login_required
def price_prediction(request):
    context = {}
    return render(request, 'code/price_prediction.html', context)
@login_required
def watchlist(request):
    context = {}
    return render(request, 'code/watchlist.html', {})

    #signup
def signup(request):
    form = CreateUserForm()
   
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password= form.cleaned_data['password1']

            )
            login(request,new_user)
            return redirect('home')
        else:
            form = CreateUserForm()
    context = {'form':form}
    return render(request, 'registration/signup.html', context)

#logout
def logoutuser(request):
    logout(request)
    messages.warning(request, 'you are successfully loged out.')

    return redirect('home')

def Stockform(request):
    context = {}
    return render(request, 'portfolio/stockform.html', context)


def add_stock(request):
    dataframe = stock_name()
    print(dataframe)    
    return render(request, 'portfolio/add_stock.html', {'dataframe':dataframe})

def add_portfolio(request):
    if request.method == 'POST':
        stock = request.POST.get('stock')
        kitta = request.POST.get('kitta')

        portfolio = Portfolio.objects.create(stock_name=stock, kitta=kitta)
        portfolio.save()

        return redirect('portfolio')
    
    return redirect('portfolio')

#views for watchlist

def add_watchlist(request):
    if request.method == 'POST':
        stock_name = request.POST.get('stock_name')

        watchlist = Watchlist.objects.create(stock_name=stock_name)


        watchlist.save()
        return redirect('watchlist')


    return render(request, 'code/watchlist_form.html')


