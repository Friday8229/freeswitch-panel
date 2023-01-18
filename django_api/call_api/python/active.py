import xml.etree.ElementTree as ET
from freeswitchESL import ESL
import psycopg2

def get_description(ext_num):
    connection = psycopg2.connect(
        database="fusionpbx", user='fusionpbx', password='zd9lEhV8hYQ8wl8tjWDJNIurSI', host='127.0.0.1', port= '5432'
    )
    
    cursor = connection.cursor()
    
    data = '[{"destination_app": "transfer", "destination_data": "%s XML 94.237.97.9"}]' % (ext_num)

    query = "SELECT destination_description FROM v_destinations WHERE destination_actions::jsonb @> %s::jsonb"
    cursor.execute(query, (data,))
    
    results = cursor.fetchall()
    
    connection.close()
    
    # print(results[0][0])
    
    result = results[0][0].split(',')

    return result

def run_fs_cli_command(host, port, command):
    con = ESL.ESLconnection(host, port, "ClueCon")
    if con.connected():
        e = con.api(command)
        e.getBody()
        data = e.getBody()
    else:
        data =  "Not connected"
    con.disconnect()
    return data

def mute_conference(host, port, command):
    con = ESL.ESLconnection(host, port, "ClueCon")
    if con.connected():
        e = con.api(command)
        e.getBody()
        data = e.getBody()
    else:
        data =  "Not connected"
    con.disconnect()
    return data

host = "127.0.0.1"
port = "8021"
command = "conference xml_list"

def check_xml_string(xml_string):
    root = ET.fromstring(xml_string)
    if len(root)==0 and root.tag == "conferences":
        return True
    else:
        return False
    
# c = run_fs_cli_command(host, port, command)
def parse_xml(xml_string):
    # parse the xml string
    root = ET.fromstring(xml_string)
    conferences = {}
    # iterate over the conferences in the xml
    for conference in root:
        conference_name = conference.attrib["name"]
        conference_uuid = conference.attrib["uuid"]
        total_active_users = conference.attrib["member-count"]
        user_uuids = []
        # iterate over the users in the conference
        # for user in conference:
        #     user_uuids.append(user.attrib["uuid"])
        #     total_active_users += 1
        conferences[conference_name] = {"conference_uuid": conference_uuid, "total_active_users": total_active_users}
    return conferences


def parsexml(xml_string):
    root = ET.fromstring(xml_string)
    conferences = {}
    for conference in root.findall('conference'):
        conference_name = conference.attrib["name"].split('@')[0]
        mute_conference(host,port,f'conference {conference_name} mute all')
        conference_uuid = conference.attrib["uuid"]
        member_uuids = []
        caller_name = []
        caller_id = []
        member_count = int(conference.attrib["member-count"])
        for member in conference.findall('members/member'):
            member_uuid = member.find("uuid").text
            member_name = member.find("caller_id_name").text
            member_id = member.find("caller_id_number").text
            member_uuids.append(member_uuid)
            caller_name.append(member_name)
            caller_id.append(member_id)
        banner_data = get_description(int(conference_name))
        conferences[conference_name] = {"conference_uuid": conference_uuid, "member_count": member_count, "member_uuids": member_uuids,
                                        "caller_names":caller_name, "caller_ids":caller_id, "font":banner_data[0], "background":banner_data[1],
                                        "url":banner_data[2]}
        
    return conferences

def get_details():
    xml = run_fs_cli_command(host, port, command)
    if check_xml_string(xml):
        return "No Queues"
    else:
        conferences = parsexml(xml)
        return conferences
    
#example of using the function
# xml_str = run_fs_cli_command(host, port, command)
# conferences = parsexml(xml_str)
# print(conferences)

# print(get_details())
