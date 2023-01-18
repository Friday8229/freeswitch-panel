import psycopg2
import pandas as pd

connection = psycopg2.connect(
   database="fusionpbx", user='fusionpbx', password='zd9lEhV8hYQ8wl8tjWDJNIurSI', host='127.0.0.1', port= '5432'
)

# command = "SELECT * FROM view_users;"

# command = "select * from master.sys.server_principals"
route = [(" SELECT u.domain_uuid,\n    u.user_uuid,\n    d.domain_name,\n    u.username,\n    u.user_status,\n    u.user_enabled,\n    u.add_date,\n    c.contact_uuid,\n    c.contact_organization,\n    (c.contact_name_given || ' '::text) || c.contact_name_family AS contact_name,\n    c.contact_name_given,\n    c.contact_name_family,\n    ( SELECT string_agg(g.group_name, ', '::text) AS string_agg\n           FROM v_user_groups ug,\n            v_groups g\n          WHERE ug.group_uuid = g.group_uuid AND u.user_uuid = ug.user_uuid) AS group_names,\n    ( SELECT string_agg(g.group_uuid::text, ', '::text) AS string_agg\n           FROM v_user_groups ug,\n            v_groups g\n          WHERE ug.group_uuid = g.group_uuid AND u.user_uuid = ug.user_uuid) AS group_uuids,\n    ( SELECT g.group_level\n           FROM v_user_groups ug,\n            v_groups g\n          WHERE ug.group_uuid = g.group_uuid AND u.user_uuid = ug.user_uuid\n          ORDER BY g.group_level DESC\n         LIMIT 1) AS group_level\n   FROM v_contacts c\n     RIGHT JOIN v_users u ON u.contact_uuid = c.contact_uuid\n     JOIN v_domains d ON d.domain_uuid = u.domain_uuid\n  WHERE 1 = 1\n  ORDER BY u.username;",)]

tables = ["v_user_groups", "v_contacts", "v_users", "v_domains"]

command = """
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='dbName'
"""

command = "select * FROM INFORMATION_SCHEMA.TABLES where 'Col' like '%tablename'"

command = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"

command = """
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES where table_name like ('%view_users')"""

command = """
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES where table_name like ("%view_users")"""

command = """
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES where table_name like ("%view_users%")"""

command = """select * from information_schema.tables where table_name like ("%view_users")"""

command = "select * from information_schema.tables where table_name in ('view_users')"

command = "\d+ view_users"

command = "select pg_get_viewdef('view_users', true)"

command = "select * from information_schema.tables where table_name in ('v_user_groups')"

command = "select * from v_user_groups"

command = "select gateway_uuid, domain_uuid, gateway from v_gateways where enabled = 'true' "

command = "select conference_name from v_conferences where conference_extension = '1100' ORDER BY conference_name"

command = "select dialplan_description from v_dialplans where dialplan_number = '1100'"

command = "select * from v_destinations where destination_uuid = 'd474def4-6c9c-40df-bb2d-384f66191543'"

command = """select destination_description, destination_number from v_destinations where destination_actions = '[{"destination_app": "transfer", "destination_data": "1100 XML 94.237.97.9"}]'"""

command = "SELECT column_name, data_type FROM pg_catalog.pg_table_def WHERE tablename = 'v_destinations';"

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)

# result = pd.read_sql_query(command, connection)

# print(f"""{result}""")

cursor = connection.cursor()

# cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = %s", ('v_destinations',))

data = '[{"destination_app": "transfer", "destination_data": "%s XML 94.237.97.9"}]' % (1100)

# print("DATA:", data)

query = "SELECT destination_description FROM v_destinations WHERE destination_actions::jsonb @> %s::jsonb"
cursor.execute(query, (data,))

# query = "SELECT * FROM {} WHERE destination_actions::jsonb @> %s::jsonb".format(table_name)
# cursor.execute(query, ('[{"destination_app": "transfer", "destination_data": "1100 XML 94.237.97.9"}]',))

# cursor.execute(query, ('[{"destination_app": "transfer", "destination_data": %s}]' % (data_value)))
# cursor.execute(query, (f'{data}'))

# query = """SELECT * FROM {} WHERE destination_actions::jsonb @> %s::jsonb""".format(table_name)
# cursor.execute(query, (data,))

# query = "SELECT * FROM {} WHERE destination_actions::jsonb @> '{\"destination_app\":\"transfer\",\"destination_data\":\"%s\"}'::jsonb".format(table_name)
# cursor.execute(query, (data_value,))


# fetch and print the results
results = cursor.fetchall()

connection.close()

for result in results:
   print(f"{result}\n")

connection.close()

# cursor = connection.cursor()

# cursor.execute(command)
 
# store all the fetched data in the ans variable
# ans = cursor.fetchall()

# ans = cursor.fetchone()

# print(ans)
    
    

 
# All dataframes hereafter reflect these changes.
# print(result)
 
# print('**RESET_OPTIONS**')
 
# # Resets the options
# pd.reset_option('all')
# print(result)

exit()
# command = """
# SELECT *
# FROM INFORMATION_SCHEMA.TABLES
# WHERE TABLE_NAME = 'view_users'"""

# command = """
# SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS  
# WHERE TABLE_NAME = 'view_users'  """

# cursor = connection.cursor()
  
# cursor.execute(command)
  
# r = cursor.fetchall()

# print(r)

# total_fields = [('group_level',), ('user_uuid',), ('contact_uuid',), ('domain_uuid',), ('user_status',), ('user_enabled',), ('add_date',), ('group_uuids',), ('contact_organization',), ('contact_name',), ('contact_name_given',), ('contact_name_family',), ('group_names',), ('domain_name',), ('username',)]

# for i in r:
#     fields = f""" 
#     field1 {i[0]}
#     field2 {i[1]}
#     field3 {i[2]}
#     field4 {i[3]}
#     field5 {i[4]}
#     field6 {i[5]}
#     field7 {i[6]}
#     field8 {i[7]}
#     field9 {i[8]}
#     field10 {i[9]}
#     field11 {i[10]}
#     field12 {i[11]}
#     field13 {i[12]}
#     field14 {i[13]}
#     field15 {i[14]}"""
    
#     print(fields)

data = {"row_count":2,"rows":[{"uuid":"6d91cd24-5e2d-4512-bfbf-f879a9e8e205","direction":"inbound","created":"2023-01-14 19:49:32","created_epoch":"1673705972","name":"sofia/external/anonymous@anonymous.invalid","state":"CS_EXECUTE","cid_name":"Anonymous","cid_num":"anonymous","ip_addr":"195.185.37.60","dest":"103","application":"bridge","application_data":"user/103@192.168.1.103","dialplan":"XML","context":"192.168.1.103","read_codec":"PCMA","read_rate":"8000","read_bit_rate":"64000","write_codec":"PCMA","write_rate":"8000","write_bit_rate":"64000","secure":"","hostname":"FusionPBX","presence_id":"","presence_data":"","accountcode":"","callstate":"ACTIVE","callee_name":"103","callee_num":"103","callee_direction":"SEND","call_uuid":"6d91cd24-5e2d-4512-bfbf-f879a9e8e205","sent_callee_name":"103","sent_callee_num":"103","initial_cid_name":"Anonymous","initial_cid_num":"anonymous","initial_ip_addr":"195.185.37.60","initial_dest":"4953719451734","initial_dialplan":"XML","initial_context":"public"},{"uuid":"d1378a04-2ffe-4730-932a-badf0b5e746e","direction":"outbound","created":"2023-01-14 19:49:32","created_epoch":"1673705972","name":"sofia/internal/103@192.168.1.100:50861","state":"CS_EXCHANGE_MEDIA","cid_name":"Anonymous","cid_num":"anonymous","ip_addr":"195.185.37.60","dest":"103","application":"","application_data":"","dialplan":"XML","context":"192.168.1.103","read_codec":"PCMA","read_rate":"8000","read_bit_rate":"64000","write_codec":"PCMA","write_rate":"8000","write_bit_rate":"64000","secure":"","hostname":"FusionPBX","presence_id":"103@192.168.1.103","presence_data":"","accountcode":"","callstate":"ACTIVE","callee_name":"103","callee_num":"103","callee_direction":"SEND","call_uuid":"6d91cd24-5e2d-4512-bfbf-f879a9e8e205","sent_callee_name":"Anonymous","sent_callee_num":"anonymous","initial_cid_name":"Anonymous","initial_cid_num":"anonymous","initial_ip_addr":"195.185.37.60","initial_dest":"103","initial_dialplan":"XML","initial_context":"192.168.1.103"}]}


connection.close()
