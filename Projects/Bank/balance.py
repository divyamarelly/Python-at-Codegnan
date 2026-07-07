from users import users

# balance function definition
def balance(account:int)->int:
    curr_amount = users[account]['balance']
    return curr_amount