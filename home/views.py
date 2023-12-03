from django.http import HttpResponse
import random
import string
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def undermaintainance(request):
    return render(request,"undermaintainance.html")

def generate_random_password(request):
    length = 12  # You can adjust the length of the password as needed
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return JsonResponse({'password': password})

