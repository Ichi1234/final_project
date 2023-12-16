from random import randint


class Admin:
    def __init__(self, database):
        self.database = database

    def all_table(self):
        for data in self.database.database:
            table_data = self.database.search(data.table_name)
            print(f"This is the data of {data.table_name} table.")
            print(table_data.table)
            print()

    def specific_table(self, table_name):
        if self.database.search(table_name):
            print(f"\nThis is the data of {table_name} table.")
            print(self.database.search(table_name).table)
        else:
            print(f"Database don't have {table_name} table in it please enter a valid table name.")

    def remove(self, person_id, list_of_table):
        for remove in list_of_table.table:
            if person_id == remove["ID"]:
                index = list_of_table.table.index(remove)
                list_of_table.table.pop(index)
        print("Updated table")
        print(list_of_table.table)

class Student:
    def __init__(self, database, user_id):
        self.database = database
        self.id = user_id

    def pending_request(self): ###TODO wait for project table and then change role to member and add user to project table
        all_pending_member = self.database.search("member")

        print("This is all of pending request that have you in.")
        print(all_pending_member.filter(lambda x: self.id in x["to_be_member"]).table)


        student_choice = input("Do you want to 'Accept' or 'Deny'? ")

        if student_choice == "Accept":

            project_id = input("Input projectID that you want to accept: ")

            #check projectID and update respond
            for response in all_pending_member.table:
                if self.id in response['to_be_member'] and project_id == response['ProjectID']:
                     response_value = response['Response']
                     if response_value == "0/2":
                         response['Response'] = "1/2"
                     elif response_value == "1/2":
                         response['Response']= "2/2"
                     else:
                         print("This project already max")
            #after accept deny other project
            for remove_everything in all_pending_member.table:
                if self.id in remove_everything['to_be_member']:
                    remove_everything['to_be_member'].remove(self.id)

        else:

            everything = input("Do you want to 'Deny' every project (Y/N): ")

            #delete every thing
            if everything == "Y":
                for remove_everything in all_pending_member.table:
                    if self.id in remove_everything['to_be_member']:
                        remove_everything['to_be_member'].remove(self.id)

            #delete only specific project
            elif everything == "N":
                project_id = input("Input projectID that you want to deny: ")

                for deny in all_pending_member.table:
                    if self.id in deny['to_be_member'] and project_id == deny['ProjectID']:
                        deny['to_be_member'].remove(self.id)


        print(all_pending_member.filter(lambda x: self.id in x["to_be_member"]).table) ###TODO delete this
        print(all_pending_member) ###TODO delete this

    def evolution(self):
        """Evolution from Student to Lead (create project) """

        all_pending_member = self.database.search("member")
        login_table = self.database.search("login")

        for remove_everything in all_pending_member.table:
            if self.id in remove_everything['to_be_member']:
                remove_everything['to_be_member'].remove(self.id)

        for change_role in login_table.table:
            if self.id == change_role['ID']:
                change_role['role'] = "lead"

        #create new project
        project_id = ""  # projectID
        for i in range(4): project_id += str(randint(0, 9))  # add 4 digit to password variable
        project_table = self.database.search("project")
        title = input("What is the Project Title? ")
        project_table.insert({'ProjectID': f"{project_id}", 'Title': f"{title}"
                , 'Lead': f"{self.id}", 'Member1': "None",
                'Member2': "None", 'Advisor': "None", 'Status': "Pending"})

class Lead:
    def __init__(self, database):
        self.database = database
    def see_pending(self):

        choose = input("See pending member or advisor? (M/A): ")

        if choose == "M":
            all_pending_member = self.database.search("member")


