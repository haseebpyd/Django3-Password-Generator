from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    character = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialcharacters'):
        character.extend(list('!@#$%^&*()_+='))
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))

    thepassword = ''
    for x in range(length):
        thepassword +=random.choice(character)
         
    return render(request, 'generator/password.html',{'password':thepassword})    

def about(request):
    return render(request, 'generator/about.html', {'url':request.GET.get('url')})