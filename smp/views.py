from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm


# Create your views here.
def home(request):
    # model = Item
    paginate_by = 2
    return render(request, 'code/home.html')
    

def portfolio(request):
    context={}
    return render(request, 'code/portfolio.html', context)

def price_prediction(request):
    context = {}
    return render(request, 'code/price_prediction.html', context)

def watchlist(request):
    context = {}
    return render(request, 'code/watchlist.html', {})
def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password= form.cleaned_data['password1']

            )
            login(request,new_user)
            return redirect('home')
        else:
            form = SignUpForm()

    return render(request, 'registration/signup.html')