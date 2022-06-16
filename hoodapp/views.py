from django.shortcuts import render

# Create your views here.
def login_user(request):
    page = 'login'
    ctx = {'page': page}
    return render(request, 'hoodapp/auth.html', ctx)

def register_user(request):
    ctx = {}
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
    ctx = {}
    return render(request, 'hoodapp/hoods.html', ctx)

def create_hood(request):
    ctx = {}
    return render(request, 'hoodapp/create-hood.html', ctx)