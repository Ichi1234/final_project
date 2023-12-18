import sys
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


    def pending_request(self, dict_to_csv, time):
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
                    if len(response['Response'].split(",")) >= 2:
                        return "This project already max."

                    elif self.name in response['to_be_member'] and project_id == response['ProjectID']:
                         if response['Response'] != "":
                            response['Response'] += "," + self.name  #accept move name to response
                         else:
                            response['Response'] += self.name

                         # add name of member to project table
                         for member in self.database.search("project").table:
                             if member['Member1'] == "None":
                                 member['Member1'] = self.name
                             else:
                                 member['Member2'] = self.name

                         # change role to member
                         for role in self.database.search("login").table:
                            if role['username'] == self.name:
                                role['role'] = "member"

                         # add date time to date response
                         for date in all_pending_member.table:
                             if self.name in date['to_be_member'].split(","):
                                 if date['Response_date'] == "":
                                    date['Response_date'] += str(time.today())
                                 else:
                                    date['Response_date'] += "," + str(time.today())

                         # after accept deny other project
                         for remove_everything in all_pending_member.table:
                            if self.name in remove_everything['to_be_member']:

                               #remove user
                               new = (remove_everything['to_be_member'].replace
                                           (self.name, "").replace(",", ""))

                               remove_everything['to_be_member'] = new


                         dict_to_csv()
                         return "Role change please login again." ###TODO test this

            else:

                everything = input("Do you want to 'Deny' every project (Y/N): ")

                #delete every thing
                if everything == "Y":
                    for remove_everything in all_pending_member.table:
                        if "," in remove_everything['to_be_member']:
                           new = (remove_everything['to_be_member'].replace
                                  (self.name, "").replace(",", ""))
                           remove_everything['to_be_member'] = new

                        else:
                            new =remove_everything['to_be_member'].replace(self.name, "")
                            remove_everything['to_be_member'] = new

                #delete only specific project
                elif everything == "N":
                    project_id = input("Input projectID that you want to deny: ")

                    for deny in all_pending_member.table:
                        if self.name in deny['to_be_member'] and project_id == deny['ProjectID']:
                            if "," in deny['to_be_member']:
                                new = deny['to_be_member'].replace(self.name, "").replace(",", "")
                                deny['to_be_member'] = new

                            else:
                                new = deny['to_be_member'].replace(self.name, "")
                                deny['to_be_member'] = new


                return "Finished"

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

        #advisor_ask_table
        advisor_ask = self.database.search("question")

        for remove_everything in all_pending_member.table:
            if self.name in remove_everything['to_be_member']:
                new = remove_everything['to_be_member'].replace(self.name, "").replace(",", "")
                remove_everything['to_be_member'] = new

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
                'Member2': "None", 'Advisor': "None", 'Status': "Ongoing"})

        # insert new value to pending_member table
        all_pending_member.insert({'ProjectID' : f"{project_id}"
                        , 'to_be_member': "", 'Response': "", 'Response_date': ""})

        #insert new value to pending_advisor table
        all_pending_advisor.insert({'ProjectID' : f"{project_id}"
                        , 'to_be_advisor': "", 'Response': "", 'Response_date': ""})

        #insert new value to question table
        advisor_ask.insert({'ProjectID': f"{project_id}", 'Lead': f"{self.name}",
                            'Question': "", 'Reply': "", 'Pending': "0", 'Advisor': ""})

        print(f"This is your project table: {project_table.filter(lambda x: x['Lead'] == self.name).table}")


class Lead:
    def __init__(self, database, user_name):
        self.database = database

        #table
        self.project_table = self.database.search("project")
        self.login = self.database.search("login")
        self.all_pending_member = self.database.search("member")
        self.all_advisor_member = self.database.search("advisor")
        self.question = self.database.search("question")

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

            if len(check['Response'].split(",")) == 2 and check['ProjectID'] == self.id_project:
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
                if response['Response'] == "":
                   print("No one response your request.")
                else:
                   print(f"This is who accept the request {response['Response']}.")

    def sent_member_request(self, sent):
        for student in self.login.table:
            if student['username'] == sent and student['role'] != "student":
                return "This person already has a project."

        for pending in self.all_pending_member.table:
            if pending['ProjectID'] == self.id_project:
                # Check if the user is already in the project or if a request has already been sent
                if self.name == sent or self.name in pending['to_be_member'].split(",") or self.name in pending['Response'].split(","):
                    return "You already sent a request to this person or this person is already in the project."

                if sent in pending['to_be_member'].split(","):
                    return "You already sent a request to this person."

                if "," in pending['Response']:
                    if len(pending['Response'].split(",")) >= 2:  # Check if the project is already full
                        return "This project is already full."
                    else:
                        pending['to_be_member'] = f"{pending['to_be_member']},{sent}" if pending['to_be_member'] else sent
                        return "Request sent!"
                else:
                    if pending['to_be_member'] != "":
                        pending['to_be_member'] += "," + sent
                    else:
                        pending['to_be_member'] += sent

                    return "Request sent!"

        return "Request sent!"

    def sent_advisor_request(self, sent): ###TODO update to new value
        for advisor in self.login.table:
            if advisor['username'] == sent:
               if advisor['role'] != "faculty" and advisor['role'] != "Advisor":
                  return "This persons isn't a faculty has project."
        for member in self.all_pending_member.table:
            if member['to_be_member'] != "":
                return "Your Project still have pending members."

        for invite in self.all_advisor_member.table:
             if invite['ProjectID'] == self.id_project:
                if len(invite['Response'].split()) >= 1 or len(invite['to_be_advisor'].split()) >= 1:
                    return "This already has pending advisor or already full."
                else:
                    invite['to_be_advisor'] += sent
                    return "Request sent!"
    def sent_project_to_advisor(self):
         # change project status
         for sent in self.project_table.table:
              if sent['Lead'] == self.name:
                  sent['Status'] = "Pending"

    def ask_advisor(self):
        user_question = input("Insert your question. ")
        for question in self.question.table:
            if question['Lead'] == self.name:
               question['Question'] = user_question

    def see_reply(self):
        for question in self.question.table:
            if question['Lead'] == self.name:
               if question['Reply'] == "":
                   print("Advisor still not answer your question.")
               else:
                   print(f"Your question is {question['Question']}.")
                   print(f"This is the answer {question['Reply']}")

class Member(Lead):
    def __init__(self, database, user_name):
        super().__init__(database, user_name)

class Faculty:
    def __init__(self, database, name):
        self.database = database
        self.name = name

    def pending_request(self, exit_function, time):
        all_pending_advisor = self.database.search("advisor")

        my_pending_advisor = all_pending_advisor.filter(lambda x: self.name in x["to_be_advisor"]).table
        if not my_pending_advisor:
            return  "No one sent you request."
        else:
            print("This is all of pending request that have you in.")
            print(all_pending_advisor.filter(lambda x: self.name in x["to_be_advisor"]).table)

            advisor_choice = input("Do you want to 'Accept' or 'Deny'? ")

            if advisor_choice == "Accept":

                project_id = input("Input projectID that you want to accept: ")

                #check projectID and update respond
                for response in all_pending_advisor.table:
                    if project_id == response['ProjectID'] and response['Response'] != "":
                        return "This project already max."

                    elif self.name in response['to_be_advisor'] and project_id == response['ProjectID']:
                         response['Response'] += self.name

                         # add name of advisor to project table
                         for advisor in self.database.search("project").table:
                              advisor['Advisor'] = self.name

                         # add name of advisor to question table
                         for add_advisor in self.database.search("question").table:
                              add_advisor['Advisor'] = self.name

                         # add date time to date response
                         for date in self.database.search("advisor").table:
                              if self.name in date['to_be_advisor'].split(","):
                                 date['Response_date'] += str(time.today())


                         # change role to advisor
                         for role in self.database.search("login").table:
                             if role['username'] == self.name:
                                 role['role'] = "advisor"

                         # after accept deny other project
                         for remove_everything in all_pending_advisor.table:
                             if self.name in remove_everything['to_be_advisor']:
                                 remove_everything['to_be_advisor'] = ""


                         print("Accepted.")
                         exit_function() #tranform dict to csv
                         return "Role change to Advisor please login again."

            else:

                everything = input("Do you want to 'Deny' every project (Y/N): ")

                #delete every thing
                if everything == "Y":
                    for remove_everything in all_pending_advisor.table:
                        if self.name in remove_everything['to_be_advisor']:
                            remove_everything['to_be_advisor'] = ""

                #delete only specific project
                elif everything == "N":
                    project_id = input("Input projectID that you want to deny: ")

                    for deny in all_pending_advisor.table:
                        if self.name in deny['to_be_advisor'] and project_id == deny['ProjectID']:
                            deny['to_be_advisor'] = ""

                return "Finished"

    def all_project(self):
        return self.database.search("project")

class Advisor:
    def __init__(self, database, user_name):
        self.name = user_name
        self.database = database
        self.project_table = self.database.search("project")
        self.question = self.database.search("question")
    def all_project(self):
        return self.project_table

    def specific_project(self):
        print(self.project_table.filter(lambda x: self.name in x["Advisor"]).table)

    def pending(self):
        new_status = ""
        for pending in self.question.table:
            if pending['Lead'] == self.name:
                if pending['Pending'] == "0":
                    new_status = "Proposal Approve"
                    increase = int(pending['Pending'])
                    increase += 1
                    pending['Pending'] = str(increase)

                elif pending['Pending'] == "1":
                    new_status = "Complete"

        for approve in self.project_table.table:
             if self.name in approve["Advisor"]:
                 # check approve status
                 approve["Status"] = new_status

    def reply_question(self):
        for reply in self.question.table:
             if reply['Advisor'] == self.name:
                 if reply['Question'] != "":
                    print(reply['Question'])
                 else:
                    print("Student didn't ask your question.")

                 answer = input("Do you want to reply? (Y/N): ")
                 if answer == "Y":
                     insert = input("Insert your answer. ")
                     reply['Reply'] = insert


