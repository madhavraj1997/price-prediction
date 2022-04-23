
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    # model = Item
    paginate_by = 2
    # return render(request, 'code/home.html')
# def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('portfolio')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            # return render(request, 'code/home.html')

    return render(request, 'code/home.html')
    
@login_required
def portfolio(request):
    context={}
    return render(request, 'code/portfolio.html', context)
@login_required
def price_prediction(request):
    context = {}
    return render(request, 'code/price_prediction.html', context)
@login_required
def watchlist(request):
    context = {}
    return render(request, 'code/watchlist.html', {})
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


def logoutuser(request):
    logout(request)
    return redirect('home')