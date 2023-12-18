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


## Login menu
![Image Alt Text](https://cdn.discordapp.com/attachments/834450256921100361/1186228653672124446/image.png?ex=65927c86&is=65800786&hm=eb2e9adaf078a28420fafeeb19015177b31f590879669c960f890766437096b4&)
#### - If you type 1 to console login menu will appear
#### - Insert correct Username and Password if not correct You need to Login again

## Student role example 
![Image Alt Text](https://cdn.discordapp.com/attachments/834450256921100361/1186248028286365746/image.png?ex=65928e91&is=65801991&hm=1c01bbf362d05bb5985e37cb7f3b2e523254c98629681c4794e673019b4660cf&)
#### - If you type 1 to console you will see. if someone send you a request to join project? and decide to join or not.
#### - If you type 2 to console User will deny every invitation from lead and Create new project.

## Member role example
![Image Alt Text](https://cdn.discordapp.com/attachments/834450256921100361/1186253661844807872/image.png?ex=659293d0&is=65801ed0&hm=fc0d0d046bae6b817728673114220707ae2bb343bea7668027dd8fb3ec1ca146&)
#### - If you type 1 to console you will see pending member table.
#### - If you type 2 to console User you will see your project table.
#### - If you type 3 to console you will ask to change title of user project
#### - If you type 4 you will see who responded to the request.

## Lead role example
![Image Alt Text](https://cdn.discordapp.com/attachments/834450256921100361/1186249809007476766/image.png?ex=65929039&is=65801b39&hm=df930dcc056262ba147e24e9d130f6e9ee0e9f012d69e9e6d432efa6768b22d4&)
#### - If you type 1 to console you will see pending member table.
#### - If you type 2 to console User you will see your project table.
#### - If you type 3 to console program will show you your project ready to solicit an advisor.
#### - If you type 4 to console you will ask to change title of user project
#### - If you type 5 you will sent an invite to become the member of the project to student
#### - If you type 6 you will sent an invite to become the advisor of the project to faculty
#### - If you type 7 you will see who responded to the request.
#### - If you type 8 you will sent your Proposal to your advisor.
#### - If you type 9 you will sent your complete project to your advisor.
#### - If you type 10 you will sent your question to your advisor.
#### - If you type 11 you will see question reply from your advisor.

## Faculty role example
![Image Alt Text](https://cdn.discordapp.com/attachments/834450256921100361/1186255126839709766/image.png?ex=6592952d&is=6580202d&hm=06c2b3d5a20b5a91bc2002565b5d7be86fb017ac5b8c01520574eee3ee7edf1e&)
#### - If you type 1 to console you will see. if someone send you a request to join project? and decide to join or not.
#### - If you type 2 to console User you will see all project table.

## Advisor role example
![Image Alt Text](https://cdn.discordapp.com/attachments/834450256921100361/1186255760053784596/image.png?ex=659295c4&is=658020c4&hm=344d9dc4ec1ce0773db3c14fd101a3078bd52e8b95bb9841fe3b5b07731a2688&)
#### - If you type 1 to console User you will see all project table.
#### - If you type 2 to console User you will see project table that you be an advisor.
#### - If you type 3 to console you will see proposal and complete project approve request.
#### - If you type 2 to console User you will see student question.



