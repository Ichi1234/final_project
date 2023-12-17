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
    def __init__(self, database, name):
        self.database = database
        self.name = name


    def pending_request(self): ###TODO wait for project table and then change role to member and add user to project table
        all_pending_member = self.database.search("member")

        my_pending_member = all_pending_member.filter(lambda x: self.name in x["to_be_member"]).table
        if not my_pending_member:
            print("No one sent you request.")
        else:
            print("This is all of pending request that have you in.")
            print(all_pending_member.filter(lambda x: self.name in x["to_be_member"]).table)

            student_choice = input("Do you want to 'Accept' or 'Deny'? ")

            if student_choice == "Accept":

                project_id = input("Input projectID that you want to accept: ")

                #check projectID and update respond
                for response in all_pending_member.table:
                    if len(response['Response']) >= 2:
                        print("This project already max.")

                    elif self.name in response['to_be_member'] and project_id == response['ProjectID']:
                         response['Response'].append(self.name) #accept move name to response


                #after accept deny other project
                for remove_everything in all_pending_member.table:
                    if self.name in remove_everything['to_be_member']:
                        remove_everything['to_be_member'].remove(self.name)

            else:

                everything = input("Do you want to 'Deny' every project (Y/N): ")

                #delete every thing
                if everything == "Y":
                    for remove_everything in all_pending_member.table:
                        if self.name in remove_everything['to_be_member']:
                            remove_everything['to_be_member'].remove(self.name)

                #delete only specific project
                elif everything == "N":
                    project_id = input("Input projectID that you want to deny: ")

                    for deny in all_pending_member.table:
                        if self.name in deny['to_be_member'] and project_id == deny['ProjectID']:
                            deny['to_be_member'].remove(self.name)


            print(all_pending_member.filter(lambda x: self.name in x["to_be_member"]).table) ###TODO delete this
            print(all_pending_member) ###TODO delete this

    def evolution(self):
        """Evolution from Student to Lead (create project) """

        #pending_member table
        all_pending_member = self.database.search("member")

        #pending advisor table
        all_pending_advisor = self.database.search("advisor")

        #login table
        login_table = self.database.search("login")

        #project table
        project_table = self.database.search("project")

        for remove_everything in all_pending_member.table:
            if self.name in remove_everything['to_be_member']:
                remove_everything['to_be_member'].remove(self.name)

        for change_role in login_table.table:
            if self.name == change_role['ID']:
                change_role['role'] = "lead"

        #create new project
        project_id = ""  # projectID
        for i in range(7): project_id += str(randint(0, 9))  # add 4 digit to password variable

        title = input("What is the Project Title? ")

        #change role to lead
        for user in login_table.table:
            if self.name == user['username']:
                user['role'] = "lead"

        #insert new value to project table
        project_table.insert({'ProjectID': f"{project_id}", 'Title': f"{title}"
                , 'Lead': f"{self.name}", 'Member1': "None",
                'Member2': "None", 'Advisor': "None", 'Status': "Pending"})

        # insert new value to pending_member table
        all_pending_member.insert({'ProjectID' : f"{project_id}"
                        , 'to_be_member': [], 'Response': [], 'Response_date': ""})

        #insert new value to pending_advisor table
        all_pending_advisor.insert({'ProjectID' : f"{project_id}"
                        , 'to_be_advisor': [], 'Response': [], 'Response_date': ""})

        print(f"This is your projectID: {project_table.filter(lambda x: x['Lead'] == self.name).table}")

class Lead:
    def __init__(self, database, user_name):
        self.database = database
        self.project_table = self.database.search("project")
        self.login = self.database.search("login")
        self.all_pending_member = self.database.search("member")
        self.all_advisor_member = self.database.search("advisor")
        self.name = user_name
        self.id_project = self.name_to_project()


    def name_to_project(self):
        #convert name to projectID
        for id_of_project in self.project_table.table:
            if id_of_project['Lead'] == self.name:
                return id_of_project['ProjectID']
    def see_pending(self):

        choose = input("See pending member or advisor? (M/A): ")

        if choose == "M":

            for pending_member in self.all_pending_member.table:
                if pending_member['ProjectID'] == self.id_project:
                    print(self.all_pending_member.filter(lambda x: self.id_project in x["ProjectID"]).table)

        elif choose == "A":

            for pending_advisor in self.all_advisor_member.table:
               if pending_advisor['ProjectID'] == self.id_project:
                   print(self.all_advisor_member.filter(lambda x: self.id_project in x["ProjectID"]).table)

    def your_project(self):
        print(self.project_table.filter(lambda x: self.id_project in x["ProjectID"]).table)
    def solicit_or_not(self):
        for check in self.all_pending_member.table:

            if len(eval(check['Response'])) == 2 and check['ProjectID'] == self.id_project:
                print("This project is ready to solicit an advisor.\n")
            else:
                print("This project still have pending member.\n")

    def change_value_of_project(self, want):
        new_value = input("Change value to? ")
        for change in self.project_table.table:
            if change['ProjectID'] == self.id_project:
                 #check if is it user project?
                 change[want] = new_value

    def check_responded(self):
        for response in self.all_pending_member.table:
            if response['ProjectID'] == self.id_project:
                if not eval(response['Response']):
                   print("No one response your request.")
                else:
                   print(f"This is who accept the request {response['Response']}.")

    def sent_member_request(self, sent):
        for student in self.login.table:
            if student['username'] == sent and student['role'] != "student":
                print("This persons already has project.")
            else:
                for invite in self.project_table.table:
                    if invite['ProjectID'] == self.id_project:
                        for pending in self.all_pending_member.table:
                            if len(eval(pending['Response'])) >= 2:
                                print("This project already full.")
                            else:
                                pending['to_be_member'] = sent

    def sent_advisor_request(self, sent):
        for advisor in self.login.table:
            if advisor['username'] == sent and advisor['role'] != "faculty":
                print("This persons already has project.")
            else:
                for invite in self.project_table.table:
                    if invite['ProjectID'] == self.id_project:
                        for pending in self.all_advisor_member.table:
                            if len(pending['Response']) >= 1 and len(pending['to_be_advisor']) >= 1:
                                print("This already has pending advisor or already full.")
                            else:
                                pending['to_be_advisor'] = sent





