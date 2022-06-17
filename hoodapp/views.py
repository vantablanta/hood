from django.shortcuts import render, redirect

from hoodapp.models import Hood, Profile
from .forms import RegisterForm

# Create your views here.
def login_user(request):
    page = 'login'
    ctx = {'page': page}
    return render(request, 'hoodapp/auth.html', ctx)

def register_user(request):
    form  = RegisterForm()
    ctx = {'form': form}
    return render(request, 'hoodapp/auth.html', ctx)

def home(request):
    ctx = {}
    return render(request, 'hoodapp/index.html', ctx)

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

def join_hood(request, name):
    hood = Hood.objects.get(name = name)
    join = False
    user = request.user 
    if request.method == 'POST':
        profile = Profile.objects.get(owner = user)
        profile.create(hood=hood)
        profile.save()

        return redirect('hood')

    ctx = {'join': join, 'obj': hood}
    return render(request, 'hoodapp/join.html', ctx)

def create_hood(request):
    ctx = {}
    return render(request, 'hoodapp/create-hood.html', ctx)