from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_1(request):
    return HttpResponse('<h1>App 1<h2/>')

def index(request):
    return render(request, 'index.html')