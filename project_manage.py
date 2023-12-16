# import database module
import sys
from database import Database, Table, Read
from random import randint
# define a funcion called initializing
db = Database()
read = Read()
# define a funcion called initializing

def initializing():

    # create an object to read all csv files that will serve as a persistent state for this program
    person_csv = read.input_csv_file("persons.csv")
    login_csv = read.input_csv_file("login.csv")

    # create all the corresponding tables for those csv files
    persons_table = Table('persons', person_csv)
    login_table = Table('login', login_csv)

    # login_table.update("7447677", 'password', '8887') ###TODO Test case for update method
    ###TODO make project table
    project_table = Table("project", [])
    advisor_pending_table = Table("advisor", [])
    member_pending_table = Table("member", [])
    # see the guide how many tables are needed

    # add all these tables to the database
    db.insert(persons_table)
    db.insert(login_table)

    print(login_table) ###TODO delete this when finish everything
def login():

    #ask info from user
    print("Welcome to Senior project report.")
    user_name = input("What is your Username?: ")
    user_pass = input("What is your Password?: ")
    #pull value from database
    login_database = db.search('login')

    #check if user input equal to database
    for check in login_database.table:
       #return the value if user input correct username and password
       if user_name == check['username'] and user_pass == check['password']: return [check['ID'], check['role']]


# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    for data in db.database:
        table_data = db.search(data.table_name)
        db.dict_to_csv(data.table_name, table_data.table)


# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
print(val) ###TODO remove this when finish

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val[1] == 'admin':
  # see and do admin related activities
   print("Hi Admin!\nWhat do you want to do today?\n\n1.See all table in Database."
        "\n2.See specific table in Database\n3.Change value of the table in Database."
         "\n4.Remove value from Database.\n5.Exit the program.\n")

   admin_command = input("Type command number in this line: ")
   print()

   #Check what admin want to do
   if admin_command == "1":
       for data in db.database:
           table_data = db.search(data.table_name)
           print(f"This is the data of {data.table_name} table.")
           print(table_data.table)
           print()

   if admin_command == "2":
       name_of_table = input("What is the table name? ")
       if db.search(name_of_table):
           print(f"\nThis is the data of {name_of_table} table.")
           print(db.search(name_of_table).table)
       else:
           print(f"Database don't have {name_of_table} table in it please enter a valid table name.")


   def check(table, key, user_value): ###TODO move this to role command.py
      for check_valid in table.table:
          if user_value == check_valid[key]:
             return True
          else:
             return False
   def check_key(table, key): ###TODO move this to role command.py
      for check_keys in table.table:
         if key not in [i for i in check_keys.keys()]:
             return False
         else:
             return True
   if admin_command == "3":
       table_name = input("What table do you want to change? ")
       # table that user want to change
       change_table = db.search(table_name)

       while not change_table: #check if table name exit in database?
           print()
           print(f"Database don't have {table_name} table in it please enter a valid table name.")
           table_name = input("What table do you want to change? ")
           print()
           change_table = db.search(table_name)

       #ID that user want to change
       person_id = input("Please insert the person id: ")
       while not check(change_table, "ID", person_id):
           print("\nPlease enter a valid person ID.")
           person_id = input("Insert the person id: ")

       #key that user want to change
       change_key = input("\nWhat key do you want to change? ")
       while not check_key(change_table, change_key):
           print("\nPlease enter a valid key.")
           change_key = input("Insert valid key: ")
       #new value
       change_value = input("\nInsert new value: ")

       #update table in database
       change_table.update(person_id, change_key, change_value)
       print(change_table)




# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
# exit()
