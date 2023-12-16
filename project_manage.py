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
    project_table = Table("project", [])
    login_table.update("7447677", 'password', '8887') ###TODO Test case for update method
    ###TODO make project table
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
    login_data = db.search('login')
    persons_data = db.search('persons')

    db.dict_to_csv('persons.csv', persons_data.table)
    db.dict_to_csv('login.csv', login_data.table)

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
print(val)
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
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
exit()
