from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from hoodapp.models import Amenity, Business, Contact, Hood, Profile, News, Comment
from .forms import AddAmenityForm, CreateHoodForm, RegisterForm, UpdateProfileForm
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
    form = RegisterForm()

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
            
            page = 'register'
            return render(request, 'hoodapp/success.html',{'page': page})
    ctx = {'form': form}
    return render(request, 'hoodapp/auth.html', ctx)

def home(request):
    ctx = {}
    return render(request, 'hoodapp/index.html', ctx)

@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        owner = Profile.objects.get(owner = request.user)

        new_message = Contact.objects.create(name= name, email=email, 
        phone=phone, subject=subject, message=message, owner = owner)
        new_message.save()

        page = 'contact'
        return render(request, 'hoodapp/success.html',{'page': page})
    ctx = {}
    return render(request, 'hoodapp/contact-us.html', ctx)

def about(request):
    ctx = {}
    return render(request, 'hoodapp/about-us.html', ctx)

@login_required(login_url='login')
def hoods(request):
    hoods = Hood.objects.all()
    member = Profile.objects.get(owner=request.user)
    ctx = {'hoods': hoods, 'member': member}
    return render(request, 'hoodapp/hoods.html', ctx)

def single_hood(request, name):
    hood = Hood.objects.get(name=name)
    amenity = Amenity.objects.filter(hood=hood)
    news = News.objects.filter(hood=hood)
    business = Business.objects.filter(hood=hood)
    comments = Comment.objects.filter(hood = hood)
    current_user = Profile.objects.get(owner=request.user)
    
    if request.method == "POST":
        body = request.POST.get('body')
        new_comment = Comment.objects.create(poster = current_user, body=body, hood=hood)
        new_comment.save()

    ctx = {'hood': hood, 'current_user': current_user, 'amenity':amenity, 'news': news, 'business': business, 'comments':comments}
    return render(request, 'hoodapp/single-hood.html', ctx)

def add_news(request, name):
    page = 'news'
    hood = Hood.objects.get(name=name)
    if request.method == 'POST':
        poster = Profile.objects.get(owner=request.user)
        title = request.POST.get('title')
        body = request.POST.get('body')
        new_news = News.objects.create(
            title=title, body=body, poster=poster, hood=hood)
        new_news.save()
        ctx = {'hood': hood}
        return redirect('hood', hood.name)
    ctx = {'page':page}
    return render(request, 'hoodapp/add.html', ctx)

def add_business(request, name):
    page = 'business'
    hood = Hood.objects.get(name=name)
    if request.method == 'POST':
        owner = Profile.objects.get(owner=request.user) 
        business_name = request.POST.get('name')
        location = request.POST.get('location')
        contact = request.POST.get('contact')
        new_business = Business.objects.create(owner=owner, name=business_name, location=location, contact=contact, hood=hood)
        new_business.save()
        return redirect('hood', hood.name)
    ctx = {'page':page}
    return render(request, 'hoodapp/add.html', ctx)

def add_amenity(request, name):
    page = 'amenity'
    form = AddAmenityForm()
    hood = Hood.objects.get(name=name)
    if request.method == 'POST':
        form = AddAmenityForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(owner = request.user)
            amenity_name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            location= form.cleaned_data['location']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            new_amenity = Amenity.objects.create(owner=profile, name=amenity_name, 
            type = type, location = location, phone = phone, email = email, hood=hood)
            new_amenity.save()
            return redirect('hood', hood.name)
    ctx = {'page':page, 'form':form}
    return render(request, 'hoodapp/add.html', ctx)

@login_required(login_url='login')
def join_hood(request, name):
    page = 'join'
    hood = get_object_or_404(Hood, name=name)
    if request.method == 'POST':
        user = Profile.objects.get(owner=request.user)
        user.hood = hood
        user.save()
        messages.success(request, 'You have successfully joined')
        return redirect('hood', hood.name)
    ctx = {'page': page, 'obj': hood}
    return render(request, 'hoodapp/join.html', ctx)

@login_required(login_url='login')
def leave_hood(request, name):
    profile = Profile.objects.get(owner = request.user)
    hood = get_object_or_404(Hood, name=name)
    profile.hood = None
    profile.save()
    messages.success(request, 'You have successfully left the hood')
    return redirect('hoods')

@login_required(login_url='login')
def create_hood(request):
    form = CreateHoodForm()
    if request.method == "POST":
        form = CreateHoodForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            img = form.cleaned_data['img']
            data = Hood.objects.create(
                name=name, admin=request.user, location=location, img=img)
            data.save()
            return redirect('hoods')
    ctx = {'form': form}
    return render(request, 'hoodapp/create-hood.html', ctx)

def user_profile(request):
    profile = Profile.objects.get(owner=request.user)
    news = News.objects.filter(poster = profile)
    ctx = {'profile': profile, 'news': news}
    return render(request, 'hoodapp/profile.html', ctx)

def update_profile(request):
    profile = Profile.objects.get(owner=request.user)
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(
            request.POST, request.FILES, instance=profile, )
        if form.is_valid():
            form.save()
            return redirect('profile')

    ctx = {'profile': profile, 'form': form}
    return render(request, 'hoodapp/update-profile.html', ctx)


def search(request):
    query  = request.GET.get('query')
    if query:
        business = Business.objects.filter(
            Q(name__icontains=query) | 
            Q(owner__owner__username__icontains=query)
        )
    ctx = {'business': business}
    return render(request, 'hoodapp/search.html', ctx)