from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from hoodapp.models import Hood, Profile, News
from .forms import CreateHoodForm, RegisterForm, UpdateProfileForm
from .emails import send_welcome_email


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

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            recipient = User(username=username, email=email)
            send_welcome_email(username, email)

            profile = Profile.objects.create(owner=user)
            profile.save()

            return render(request, 'hoodapp/success.html')
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

@login_required(login_url='login')
def hoods(request):
    hoods = Hood.objects.all()
    member = Profile.objects.get(owner = request.user)
    ctx = {'hoods': hoods, 'member': member}
    return render(request, 'hoodapp/hoods.html', ctx)

def single_hood(request, name):
    hood = Hood.objects.get(name = name)
    news = News.objects.filter(hood = hood)
    current_user = Profile.objects.get(owner = request.user)

    if request.method == 'POST':
        poster = Profile.objects.get(owner = request.user)
        title = request.POST.get('title')
        body = request.POST.get('body')
        new_news = News.objects.create(title = title, body =body, poster = poster, hood =hood)
        new_news.save()

    ctx = {'hood': hood, 'current_user': current_user, 'news':news}
    return render(request, 'hoodapp/single-hood.html', ctx)

@login_required(login_url='login')
def join_hood(request, name):
    page = 'join'
    hood = get_object_or_404(Hood, name=name)
    if request.method == 'POST':
        user = Profile.objects.get(owner =request.user)
        user.hood = hood
        user.save()
        messages.success(request, 'You have successfully joined')
        return redirect('hood', hood.name)
    ctx = {'page':page, 'obj': hood}
    return render(request, 'hoodapp/join.html', ctx)

@login_required(login_url='login')
def leave_hood(request, name):
    hood = get_object_or_404(Hood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('hood')

@login_required(login_url='login')
def create_hood(request):
    form  = CreateHoodForm()
    if request.method == "POST": 
        form = CreateHoodForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            img = form.cleaned_data['img']
            data = Hood.objects.create(name=name, admin=request.user, location=location, img=img)
            data.save()
            return redirect('hoods')
    ctx = {'form': form}
    return render(request, 'hoodapp/create-hood.html', ctx)

def user_profile(request):
    profile = Profile.objects.get(owner = request.user)
    ctx = {'profile': profile}
    return render(request, 'hoodapp/profile.html', ctx)

def update_profile(request):
    profile = Profile.objects.get(owner = request.user)
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile, )
        if form.is_valid():
            form.save()
            return redirect('profile')

    ctx = {'profile': profile, 'form':form}
    return render(request, 'hoodapp/update-profile.html', ctx)

