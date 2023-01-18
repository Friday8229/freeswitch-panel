from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from subprocess import call, PIPE, Popen
from . api import get_details
import pandas as pd
import psycopg2

connection = psycopg2.connect(
   database="fusionpbx", user='fusionpbx', password='zd9lEhV8hYQ8wl8tjWDJNIurSI', host='127.0.0.1', port= '5432'
)

# Create your views here.
def home(request):
    
    context = {}
    
    get_users()
    
    return render(request, 'call_api/home.html', context)

@api_view(['POST'])
def mod_conf(request):
    
    # details = request.data['details']
    details = request.POST.getlist('details')
    
    number = details[0]
    room = details[1]
    
    py_file = "/home/freeswitch/freeswitch_api/django_api/call_api/python/test.py"
    py_env = "/home/freeswitch/esl_env/bin/python2.7"
    
    process = call(f'sudo {py_env} {py_file} {number} {room}', shell=True)

    return Response('HOI HOI')

@api_view(['POST'])
def active_call(request):
    
    # details = request.data['details']
    details = request.POST.getlist('details')
    
    host = "127.0.0.1"
    port = "8021"
    command = "show channels as json"
    
    c = run_fs_cli_command(host, port, command)
    
    print(c)
    
    if int(c["row_count"]) > 0:
    
        for item in c['rows']:
            print(item['uuid'])

    return Response(c)

@api_view(['POST'])
def active_calls(request):
    
    # details = request.data['details']
    details = request.POST.getlist('details')
    
    host = "127.0.0.1"
    port = "8021"
    command = "show channels as json"
    
    data = get_details()

    return Response(data)

@api_view(['POST'])
def ApiReq(request):
    
    details = request.data['details']
    
    if details == 'conferences':
        command = "select conference_name,conference_extension,conference_pin_number,conference_description,conference_enabled from v_conferences ORDER BY conference_name"
        result = pd.read_sql_query(command, connection)
        
        print("LENGTH", len(result.values.tolist()))
        
        return Response(result.values.tolist())
    elif details == 'extensions':
        command = "select enabled, description, call_group, extension, password from v_extensions"
        result = pd.read_sql_query(command, connection)
        
        print("LENGTH", len(result.values.tolist()))
        
        return Response(result.values.tolist())
    elif details == 'users':
        command = f"select username,user_email, user_status from v_users"
        result = pd.read_sql_query(command, connection)
        
        return Response(result.values.tolist())
    else: 
        return Response('404')
    
    # process = call(f'/root/call_center/python_scripts/call.sh {number}', shell=True)