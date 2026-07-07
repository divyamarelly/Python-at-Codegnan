from users import users

# Transfer Function Definition
def transfer(sender:int, reciever:int, transfer_amount:int):
    if reciever in users:
        curr_amount = users[sender]['balance']
        if curr_amount >= transfer_amount:
            users[sender]['balance'] -= transfer_amount
            users[reciever]['balance'] += transfer_amount
            return f"{transfer_amount} Transfer successful and \
            Current Balance is {users[sender]['balance']}"
        return "Insufficient Balance"
    return "Reciever account not found"