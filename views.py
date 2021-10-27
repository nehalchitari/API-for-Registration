from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'users/home.html')

def s(request):
    return HttpResponse(request, 'hi...')

def p(request):
    return HttpResponse(request, 'hii..')

def r(request):
    return HttpResponse(request, 'hiii..')

def t(request):
    return HttpResponse(request, 'hiiii..')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()


    return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')







