
def check(table, key, user_value):
     for check_valid in table.table:
        if user_value == check_valid[key]:
            return True
        else:
            return False

def check_key(table, key):
    for check_keys in table.table:
        if key not in [i for i in check_keys.keys()]:
            return False
        else:
            return True

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

    def update_table(self, table_name, id_person, key_change, new_value):
        # update table in database
        table_name.update(id_person, key_change, new_value)
        print("New value")
        print(table_name.filter(lambda x: x[key_change] == new_value))

