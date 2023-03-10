import requests
from subprocess import call
from django.conf import settings
from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='login')
def home(request):
    
    context = {}
    
    return render(request, 'front_panel/home.html', context)

def AdminPanel(request):
    
    context = {}
    
    return render(request, 'front_panel/admin_panel.html', context)

def dashboard(request):
    
    context = {}
    
    return render(request, 'front_panel/dashboard.html', context)

def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    
    return render(request, 'front_panel/login.html', context)


def Register(request):
    
    context = {}
    
    return render(request, 'front_panel/home.html', context)

@api_view(['POST'])
def Make_Call(request):
    
    details = request.data['details']
    
    print(details)
    
    number = details[1]
    
    # process = call(f'/root/call_center/python_scripts/call.sh {number}', shell=True)
    
    return Response("Hoi")

@api_view(['POST'])
def fetch_data(request):
    
    data = request.data['details']
    
    post_data = {'details': data}
    response = requests.post('http://94.237.97.9:8000/api_req/', data=post_data)
    content = response.content
    
    # options:
    # conferences
    # extensions
    # users
    
    # process = call(f'/root/call_center/python_scripts/call.sh {number}', shell=True)
    
    return Response(content)

@api_view(['POST'])
def active_calls(request):
    
    # data = request.data['details']
    
    response = requests.post('http://94.237.97.9:8000/api_activeCalls/')
    
    content = response.content
    
    print(content)
    
    return Response(content)

@api_view(['POST'])
def conference(request):
    
    data = request.data['details']
    
    post_data = {'details': data}
    response = requests.post('http://94.237.97.9:8000/api_conf/', data=post_data)
    content = response.content
    
    # options:
    # conferences
    # extensions
    # users
    
    # process = call(f'/root/call_center/python_scripts/call.sh {number}', shell=True)
    
    return Response(content)