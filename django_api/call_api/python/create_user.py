import time
import random
import string
import psycopg2
import pandas as pd
from uuid import uuid4

connection = psycopg2.connect(
   database="fusionpbx", user='fusionpbx', password='Cp0Wg8Zz5JhsuvGnn7t8ORh1Do', host='127.0.0.1', port= '5432'
)

cursor = connection.cursor()

salt = None
add_user = "admin"
domain_name = "167.99.241.212"
date = "2022-11-25 10:57:56.000000+0000"
date_time = time.strftime('%Y-%m-%d %H:%M:%S')
domain_uuid = "05c47508-d57f-47f7-a015-73141819f4bd"
agent = "4921e3d2-0fb4-4de4-b5e1-01a2e91b0262"
superadmin = "efd515db-9b16-4701-a614-a2c437a5e25d"

def ran(char_length):
    characters = string.ascii_lowercase + string.digits
    v = ''.join(random.choice(characters) for i in range(char_length))
    return v

def uuid():
    return str(uuid4())

print("UUID:", uuid())

def add_user(username, user_status, user_enabled, add_date, contact_uuid, contact_organization, contact_name, contact_name_given, contact_name_family, group_names, group_uuids, group_level):
    command = f"""
    INSERT INTO view_users
    (domain_uuid, user_uuid, domain_name, username, user_status, user_enabled, add_date, contact_uuid, contact_organization, contact_name, contact_name_given, contact_name_family, group_names, group_uuids, group_level)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    uu = uuid()

    data_to_insert = (domain_uuid, uu, domain_name, username, user_status,
                      user_enabled, add_date, contact_uuid, contact_organization,
                      contact_name, contact_name_given, contact_name_family,
                      group_names, group_uuids, group_level)
    
    cursor.execute(command, data_to_insert)


add_user("Taylor", "Available", True, "2022-11-26 16:31:23.000000+0000",
         f"{uuid()}", "cc", "Tylor s", "Tylor", "s", "agent", agent, 20.0)

connection.commit()