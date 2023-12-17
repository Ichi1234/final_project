# import database module
import sys
from database import Database, Table, Read
from role_commands import Admin, Student, Lead, Member, Faculty, Advisor
from datetime import date
from random import randint
# define a function called initializing
db = Database()
read = Read()

# define a function called initializing

def initializing():

    # create an object to read all csv files that will serve as a persistent state for this program
    person_csv = read.input_csv_file("persons.csv")
    login_csv = read.input_csv_file("login.csv")
    project_csv = read.input_csv_file("project.csv")
    member_csv = read.input_csv_file("member.csv")
    advisor_csv = read.input_csv_file("advisor.csv")
    advisor_response_csv = read.input_csv_file("question.csv")

    # create all the corresponding tables for those csv files
    persons_table = Table('persons', person_csv)
    login_table = Table('login', login_csv)


    project_table = Table("project", project_csv)
    advisor_pending_table = Table("advisor", advisor_csv)
    advisor_response_table = Table("question", advisor_response_csv)
    member_pending_table = Table("member", member_csv)
    # see the guide how many tables are needed

    # add all these tables to the database
    db.insert(persons_table)
    db.insert(login_table)
    db.insert(project_table)
    db.insert(advisor_pending_table)
    db.insert(member_pending_table)
    db.insert(advisor_response_table)

    print(login_table) ###TODO delete this when finish everything


def check(table, key, user_value):
    multiple = False
    for check_valid in table.table:
        if user_value == check_valid[key]:
            multiple = True

    return multiple


def check_key(table, key):
    answer = False
    for check_keys in table.table:
        if key in [i for i in check_keys.keys()]:
            answer = True

    return answer
def id_to_name(user_id):
    login_table = db.search("login")
    for i in login_table.table:
        if i['ID'] == user_id:
            return i['username']

def name_to_id(user_name):
    login_table = db.search("login")
    for i in login_table.table:
        if i['username'] == user_name:
            return i['ID']

def login():

    #ask info from user
    print("Welcome to Senior project report.")
    user_name = input("What is your Username?: ")
    user_pass = input("What is your Password?: ")

    #pull value from database
    login_database = db.search('login')

    #check if user input equal to database
    for equal in login_database.table:
       #return the value if user input correct username and password
       if user_name == equal['username'] and user_pass == equal['password']: return [equal['ID'], equal['role']]



# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit
def check_table():
    table_name = input("What table do you want to change? ")
    # table that user want to change
    change_table = db.search(table_name)

    while not change_table:  # check if table name exit in database?
        print()
        print(f"Database don't have {table_name} table in it please enter a valid table name.")
        table_name = input("What table do you want to change? ")
        print()
        change_table = db.search(table_name)
    return change_table

def update_table(table_name, id_person, key_change, new_value):
    # update table in database
    table_name.update(id_person, key_change, new_value)
    print("New value")
    print(table_name.filter(lambda x: x[key_change] == new_value).table)


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
#check is username and password correct
if not val:
    print("Your Username or Password is wrong. Please try again next time")
    print('"Git Gud"')
    sys.exit()



# based on the return value for login, activate the code that performs activities according to the role defined for that person_id
id_name = id_to_name(val[0])

if val[1] == 'admin':
  # see and do admin related activities
   print("--------------------------------------------------------------------------------------")
   admin = Admin(db)
   print("Hi Admin!\nWhat do you want to do today?\n\n1.See all table in Database."
        "\n2.See specific table in Database\n3.Change value of the table in Database."
         "\n4.Remove value from Database.\n0.Exit the program.\n")

   admin_command = input("Type command number in this line: ")
   print()

   while admin_command != "0": #Escape from program:
       #Check what admin want to do
       if admin_command == "1": #user want to see every table
           admin.all_table()

       if admin_command == "2": #user want to see specific table
           name_of_table = input("What is the table name? ")
           admin.specific_table(name_of_table)

       if admin_command == "3": #user want to change value
           user_table = check_table()

           #ID that user want to change
           person_id = input("Please insert the person id: ")
           print(user_table)
           print(check(user_table, "ID", person_id))
           while not check(user_table, "ID", person_id):
               print("\nPlease enter a valid person ID.")
               person_id = input("Insert the person id: ")

           #key that user want to change
           change_key = input("\nWhat key do you want to change? ")
           while not check_key(user_table, change_key):
               print("\nPlease enter a valid key.")
               change_key = input("Insert valid key: ")

           #new value
           change_value = input("\nInsert new value: ")

           #update table in database
           update_table(user_table, person_id, change_key, change_value)

       if admin_command == "4": #user want to remove someone
           remove_table = check_table() #input table

           #input person_ID
           person_id = input("Please insert the person id: ")
           while not check(remove_table, "ID", person_id):
               print("\nPlease enter a valid person ID.")
               person_id = input("Insert the person id: ")

           admin.remove(person_id, remove_table)
       print("--------------------------------------------------------------------------------------")
       print("Hi Admin!\nWhat do you want to do today?\n\n1.See all table in Database."
             "\n2.See specific table in Database\n3.Change value of the table in Database."
             "\n4.Remove value from Database.\n0.Exit the program.\n")

       admin_command = input("Type command number in this line: ")

elif val[1] == 'student':
    student = Student(db, id_name)
    print("--------------------------------------------------------------------------------------")
    # see and do student related activities
    print("Welcome student!\nWhat do you want to do today?\n\n1.See pending requests."
          "\n2.Become lead (Deny all request)"
          "\n0.Exit Program")
    student_command = input("\nType command number in this line: ")
    print()
    while student_command != "0":
        if student_command == "1": # see pending requests
            student.pending_request(exit, date)
        if student_command == "2": # become lead student
            student.evolution()
            exit()
            sys.exit()

        print("--------------------------------------------------------------------------------------")
        print("Welcome student!\nWhat do you want to do today?\n\n1.See pending requests."
              "\n2.Become lead (Deny all request)"
              "\n0.Exit Program")
        student_command = input("\nType command number in this line: ")

elif val[1] == 'member':
    member = Member(db, id_name)
    print("--------------------------------------------------------------------------------------")
    # see and do member related activities
    print("Welcome Member!\nWhat do you want to do today?\n\n1.See pending requests."
          "\n2.See your project info"
          "\n3.Change value of project table in Database"
          "\n4.See who responded to the request.")
    member_command = input("\nType command number in this line: ")
    print()

    while member_command != "0":

        if member_command == "1":
            member.see_pending()

        if member_command == "2":
            member.your_project()

        if member_command == "3":
            user_change = input("What key do you want to change? ")
            while not check_key(db.search("project"), user_change):
                print("\nPlease enter a valid key.")
                user_change = input("Insert valid key: ")

            member.change_value_of_project(user_change)

        if member_command == "4":
            member.check_responded()

        print("--------------------------------------------------------------------------------------")
        # see and do member related activities
        print("Welcome Member!\nWhat do you want to do today?\n\n1.See pending requests."
              "\n2.See your project info"
              "\n3.Change value of project table in Database"
              "\n4.See who responded to the request."
              "\n0.Exit the Program")

        member_command = input("\nType command number in this line: ")

elif val[1] == 'lead':
    print("--------------------------------------------------------------------------------------")

    lead = Lead(db, id_name)
    # see and do lead related activities
    print("Welcome Leader!\nWhat do you want to do today?\n\n1.See pending requests."
          "\n2.See your project info."
          "\n3.Check if your project ready to solicit an advisor."
          "\n4.Change value of project table in Database."
          "\n5.Sent member request.\n6.Sent advisor request.\n7.See who responded to the request."
          "\n8.Sent Proposal."
          "\n9.Sent Completed Project."
          "\n10.Ask Advisor a question."
          "\n11.See reply from Advisor."
          "\n0.Exit the Program")

    lead_command = input("\nType command number in this line: ")
    while lead_command != "0":  # Escape from program:

        if lead_command == "1": # see pending request
            lead.see_pending()

        if lead_command == "2": # see your project detail
            lead.your_project()

        if lead_command == "3": # is project ready to solicit an advisor
            lead.solicit_or_not()

        if lead_command == "4": # change value in project table
            user_change = input("What key do you want to change? ")
            while not check_key(db.search("project"), user_change):
                print("\nPlease enter a valid key.")
                user_change = input("Insert valid key: ")

            lead.change_value_of_project(user_change)


        if lead_command == "5": # sent member request

            sent = input("What is the personID you want to sent request? ")
            while not check(db.search("login"), "ID", sent):
                print("\nInvalid personID")
                sent = input("Type correct ID ")
            name_of_id = id_to_name(sent)
            print(lead.sent_member_request(name_of_id))

        if lead_command == "6": # sent advisor request

            sent = input("What is the personID you want to sent request? ")
            while not check(db.search("login"), "ID", sent):
                print("\nInvalid personID")
                sent = input("Type correct ID ")
            name_of_id = id_to_name(sent)
            print(lead.sent_advisor_request(name_of_id))

        if lead_command == "7": # see who respond the request
             lead.check_responded()

        if lead_command == "8": # sent proposal
             lead.sent_project_to_advisor()

        if lead_command == "9": # sent complete project
             lead.sent_project_to_advisor()

        if lead_command == "10":
            lead.ask_advisor()

        if lead_command == "11":
            lead.see_reply()
        print("--------------------------------------------------------------------------------------")

        print("Welcome Leader!\nWhat do you want to do today?\n\n1.See pending requests."
              "\n2.See your project info."
              "\n3.Check if your project ready to solicit an advisor."
              "\n4.Change value of project table in Database."
              "\n5.Sent member request.\n6.Sent advisor request.\n7.See who responded to the request."
              "\n8.Sent Proposal."
              "\n9.Sent Completed Project."
              "\n10.Ask Advisor a question."
              "\n11.See reply from Advisor."
              "\n0.Exit the Program")
        lead_command = input("Type command number in this line: ")

elif val[1] == 'faculty':
    faculty = Faculty(db, id_name)
    # see and do faculty related activities
    print("--------------------------------------------------------------------------------------")
    print("Welcome Faculty!\nWhat do you want to do today?\n\n1.See pending requests."
          "\n2.See details of all project."
          "\n0.Exit the program")

    faculty_command = input("\nType command number in this line: ")

    while faculty_command != "0":

        if faculty_command == "1":
            print(faculty.pending_request(exit))

        if faculty_command == "2":
            print(faculty.all_project())

        print("--------------------------------------------------------------------------------------")
        print("Welcome Faculty!\nWhat do you want to do today?\n\n1.See pending requests."
              "\n2.See details of all project."
              "\n0.Exit the program")
        faculty_command = input("\nType command number in this line: ")

elif val[1] == 'advisor':
    advisor = Advisor(db, id_name)
    # see and do advisor related activities
    print("--------------------------------------------------------------------------------------")
    print("Welcome Faculty!\nWhat do you want to do today?\n\n1.See details of all project."
          "\n2.See details of your project."
          "\n3.See pending request."
          "\n4.See Student Question."
          "\n0.Exit the program")

    advisor_command = input("\nType command number in this line: ")

    if advisor_command == "1":
        print(advisor.all_project())

    if advisor_command == "2":
        advisor.specific_project()

    if advisor_command == "3":
        advisor.pending()

    if advisor_command == "4":
        advisor.reply_question()

# once everything is done, make a call to the exit function
exit()
