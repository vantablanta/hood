from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {}
    return render(request, 'hoodapp/index.html', ctx)