import xml.etree.ElementTree as ET
from freeswitchESL import ESL
import json

def run_fs_cli_command(host, port, command):
    con = ESL.ESLconnection(host, port, "ClueCon")
    if con.connected():
        e = con.api(command)
        e.getBody()
        data = json.loads(e.getBody())
    else:
        data = "Not connected"
    con.disconnect()
    return data

host = "127.0.0.1"
port = "8021"
command = "show channels as json"

c = run_fs_cli_command(host, port, command)

if int(c["row_count"]) > 0:
    
    for item in c['rows']:
        i = item['uuid']
        print(f"uuid_transfer {i} queue queue_new")