from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, 'webapp/home.html')


@login_required
def login(request):
    return render(request, 'webapp/mybase.html')


def logout(request):
    return render(request, 'webapp/logout.html')


def contact(request):
    return render(request, 'webapp/contact.html')


def servi(request):
    return render(request, 'webapp/service.html')

def rsuccess(request):
    return render(request, 'webapp/rsuccess.html')


def err(request):
    return render(request, 'webapp/err.html')

@login_required
def show(request):
    return render(request, 'webapp/show.html')


@login_required
def shoping(request):
    return render(request, 'webapp/shoping.html')

@login_required
def food(request):
    return render(request, 'webapp/food.html')

@login_required
def hotel(request):
    return render(request, 'webapp/hotel.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rsuccess')
    else:
        form = UserCreationForm()
    return render(request, 'webapp/registration.html', {'form': form})