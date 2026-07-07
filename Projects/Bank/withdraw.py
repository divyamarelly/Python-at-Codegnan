from users import users

# withdraw function definition
def withdraw(account:int, withdraw_amount:int)->str:
    curr_amount = users[account]['balance']
    # check amount
    if curr_amount >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdrawal successful and \
            Current Balance is {users[account]['balance']}"
    return "Insufficient Balance"