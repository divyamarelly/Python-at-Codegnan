from users import users

# Deposit Function Definiton
def deposit(account:int, deposit_amount:int):
    users[account]['balance'] += deposit_amount
    return f"{deposit_amount} Deposit successful and \
        Current Balance is {users[account]['balance']}"