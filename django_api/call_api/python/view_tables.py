import psycopg2
import pandas as pd

connection = psycopg2.connect(
   database="fusionpbx", user='fusionpbx', password='zd9lEhV8hYQ8wl8tjWDJNIurSI', host='127.0.0.1', port= '5432'
)

tables = ["v_user_groups", "v_contacts", "v_users", "v_domains"]

def print_table(p_table):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    for i in p_table:
        print(f"DISPLAYING: {i}")
        
        command = f"select * from {i}"
        result = pd.read_sql_query(command, connection)

        print(f"{result}")
        
        print("#"*200)
        
    pd.reset_option('all')
    
def data():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
    command = f"select username,user_email, user_status from v_users"
    result = pd.read_sql_query(command, connection)

    print(f"{result}", result.values.tolist())
    
    pd.reset_option('all')
    
def extensions():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
    # command = "select * from v_extensions"
    
    command = "select enabled, description, call_group, extension, password from v_extensions"
    
    result = pd.read_sql_query(command, connection)

    print(f"{result}")
    
    pd.reset_option('all')
    
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

    print(f"{result}")
    
    # pd.reset_option('all')
    
def check_view(p_table):
    for i in p_table:
        print(f"Checking {i}")
        
        command = f"select * from information_schema.tables where table_name in ('{i}')"
        
        cursor = connection.cursor()

        cursor.execute(command)

        ans = cursor.fetchone()
        
        # print(ans)
        # print("COMMAND:", command)
        # print("TYPE:", ans)
        
        if ans == None:
            print("None")
        else:
            if 'BASE TABLE' in ans:
                print("It is a table")
            elif 'VIEW' in ans:
                print("It is a view")
            else:
                print("Nothing found :(")
                
        print("")
    
# print_table('v_user_groups')
# print_table('v_conctacts')
# print_table('v_users')
# print_table('v_domains')

# check_view(tables)

# print_table(tables)

# data()

# conferences()

extensions()