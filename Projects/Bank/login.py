from users import users

def login(account:int, password:str)->bool:
    # check account exists in users or not
    if account in users:
        if password == users[account]['password']:
            return True
        return False
    return False