# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file
import copy
import csv, os

class Read:
    def __init__(self):
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def input_csv_file(self, csv_name):

        csv_list = []
        with open(os.path.join(self.__location__, csv_name)) as f:
            rows = csv.DictReader(f)
            for i in rows:
                csv_list.append(dict(i))

        return csv_list

# add in code for a Database class
class Database:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
             if table.table_name == table_name:
                return table
        return None
    def dict_to_csv(self, csv_name, all_value):
        csv_file = open(f"{csv_name}", 'w')
        writer = csv.writer(csv_file)

        writer.writerow([all_value[0].keys()])
        for dictionary in all_value:
            writer.writerow(dictionary.values())
        csv_file.close()
        csv_file = open(f"{csv_name}", 'r')
        print(csv_file.read())
        csv_file.close()
# add in code for a Table class
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table
    def insert(self, info):
        self.table.append(info)
    def update(self, person_id, key_name, new_value):
        for find in self.table:
           if find['ID'] == person_id:
                 find[key_name] = new_value
    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            temps.append(float(item1[aggregation_key]))
        return function(temps)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def __str__(self):
        return self.table_name + ':' + str(self.table)


# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
