# Senior Project Report
## All role and method.
| Role     | Action                                                      | Method       | Class   | Completion |
|----------|-------------------------------------------------------------|--------------|---------|-----------:|
| developer | import all csv file from local                             | initializing  | None   |  100% |
| developer | delete to_be_member value in database when member in the project = 2| destroy_pending_member  | None   | 100% |
| developer | check if user insert correct value                         | check  | None   |  100% |
| developer | check if user insert correct key                          | check_key | None   |   100% |
| developer | check if user insert correct table                    | check_table | None   |  100% |
| developer | convert id of person to name of person                     | id_to_name  | None   |   100% |
| developer | convert name of person to id of person                     | name_to_id  | None   |   100% |
| developer | display login menu to console                             | login  | None   | 100% |
| developer | change value in table in database                                    | update_table  | None   | 100% |
| developer | convert table to csv                                    | exit | None   |       100% |
| admin    | See all of the table in Database class                      | all_table    | Admin   |       100% |
| admin    | See specific table in Database                              | specific_table | Admin   |     100% |
| admin    | Remove value from Database.                                 | admin.remove | Admin   |       100% |
| student  | See pending requests and Decide to be member or not. | pending_request | Student |       100% |
| student  | Change role from student to leader and create new project. | evolution  | Student |       100% |
| member  | All of the function inherit from Lead class | None  | Member |       100% |
| lead  | See pending requests. | see_pending  | Lead |       100% |
| lead  | See user project info. | your_project  | Lead |       100% |
| lead  | Check if your project ready to solicit an advisor. |   solicit_or_not  | Lead |       100% |
| lead  | Change title of project. | change_value_of_project  | Lead |       100% |
| lead  | Sent member request. | sent_member_request | Lead |       100% |
| lead  | Sent advisor request. |sent_advisor_request | Lead |       100% |
| lead  | See who responded to the request. | check_responded | Lead |       100% |
| lead  | Sent Proposal and Complete Project to advisor. | sent_project_to_advisor | Lead |       100% |
| lead  | Ask Advisor a question. | ask_advisor | Lead |       100% |
| lead  | See reply from Advisor. | see_reply | Lead |       100% |
| faculty  | See pending requests and decide accept or not. | pending_request | Faculty |       100% |
| faculty  | See details of all project. | all_project | Faculty |       100% |
| advisor  | See details of all project. | all_project | Advisor |       100% |
| advisor  | See details of project that has user in it. | all_project | Advisor |       100% |
| advisor  | See pending request from lead. | all_project | Advisor |       100% |
| advisor  | See Student Question and decide to reply or not. | all_project | Advisor |       100% |

## List of Files
   * **Python Files**
      - **project_manage.py**
         - This is main.py
      - **database.py**
         - This file have Table class and Database class in it
      - **role_commands**
         - This file have every role class in it
    * **CSV Files**
       - **advisor.csv**
       - **login.csv**
       - **member.csv**
       - **persons.csv**
       - **project.csv**
       - **question.csv**

           



## Step by step guide
![Image Alt Text](https://cdn.discordapp.com/attachments/1186225788551438376/1186225811913724084/image.png?ex=659279e0&is=658004e0&hm=42a96eed8dba7961c930c163deaae0bd072900dbaf8d2ee28e597ee45d4bcbb8&)

## When you press run you will see this menu in console
#### - If you type 0 to console program will end
#### - If you type 1 to console login menu will appear

![Image Alt Text](https://cdn.discordapp.com/attachments/834450256921100361/1186228653672124446/image.png?ex=65927c86&is=65800786&hm=eb2e9adaf078a28420fafeeb19015177b31f590879669c960f890766437096b4&)

## Login menu
#### - If you type 1 to console login menu will appear
#### - Insert correct Username and Password if not correct You need to Login again

## Student role example 
#### - If you type 1 to console login menu will appear

