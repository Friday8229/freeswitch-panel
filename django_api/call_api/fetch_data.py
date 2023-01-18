import psycopg2
import pandas as pd

connection = psycopg2.connect(
   database="fusionpbx", user='fusionpbx', password='zd9lEhV8hYQ8wl8tjWDJNIurSI', host='127.0.0.1', port= '5432'
)

def get_users():
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', None)
    
    command = f"select username,user_email, user_status from v_users"
    result = pd.read_sql_query(command, connection)

    # print(f"{result}", result.values.tolist())
    
    # return result.values.tolist()
    
    # pd.reset_option('all')
    
    return result.values.tolist()

def get_extensions():
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', None)
    
    command = f"select username,user_email, user_status from v_users"
    result = pd.read_sql_query(command, connection)

    # print(f"{result}", result.values.tolist())
    
    # return result.values.tolist()
    
    # pd.reset_option('all')
    
    return result.values.tolist()

def conferences():
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', None)
    
    # command = f"select * from v_conference_profiles"
    # command = f"select * from v_conference_users"
    # command = "select * from v_conferences"
    
    command = "select conference_name,conference_extension,conference_pin_number,conference_description,conference_enabled from v_conferences"
    result = pd.read_sql_query(command, connection)

    return result.values.tolist()
    
    # pd.reset_option('all')
    
def extensions():
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', None)
    
    # command = "select * from v_extensions"
    
    command = "select enabled, description, call_group, extension, password from v_extensions"
    
    result = pd.read_sql_query(command, connection)

    # print(f"{result}")
    
    # pd.reset_option('all')
    
    return result.values.tolist()