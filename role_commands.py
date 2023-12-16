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