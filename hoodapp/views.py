from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from hoodapp.models import Hood, Profile
from .forms import RegisterForm

# Create your views here.
def login_user(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password doesnt exist')
    ctx = {'page': page}
    return render(request, 'hoodapp/auth.html', ctx)

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form  = RegisterForm()
    ctx = {'form': form}
    return render(request, 'hoodapp/auth.html', ctx)

def home(request):
    ctx = {}
    return render(request, 'hoodapp/index.html', ctx)

@login_required(login_url='login')
def contact(request):
    ctx = {}
    return render(request, 'hoodapp/contact-us.html', ctx)

def about(request):
    ctx = {}
    return render(request, 'hoodapp/about-us.html', ctx)

def hoods(request):
    hoods = Hood.objects.all()
    ctx = {'hoods': hoods}
    return render(request, 'hoodapp/hoods.html', ctx)

def single_hood(request, name):
    hood = Hood.objects.get(name = name)
    ctx = {'hood': hood}
    return render(request, 'hoodapp/single-hood.html', ctx)

@login_required(login_url='login')
def join_hood(request, name):
    page = 'join'
    hood = get_object_or_404(Hood, name=name)
    if request.method == 'POST':
        request.user.profile.hood = hood
        request.user.profile.save()
        messages.success(request, 'You have successfully joined {hood.name}')
        return redirect('hood')
    ctx = {'page':page, 'obj': hood}
    return render(request, 'hoodapp/join.html', ctx)

def leave_hood(request, name):
    hood = get_object_or_404(Hood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('hood')

@login_required(login_url='login')
def create_hood(request):
    ctx = {}
    return render(request, 'hoodapp/create-hood.html', ctx)