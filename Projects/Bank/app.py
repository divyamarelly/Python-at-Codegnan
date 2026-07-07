from login import login
from balance import balance
from withdraw import withdraw
from deposit import deposit
from transfer import transfer
from ministatement import ministatement
from logout import logout
from register import register

# main
if __name__=="__main__":
    print("Welcome to the small scale bank")
    print("1. Register \n 2. Login")
    choice = int(input("Select your choice:"))
    
    # calling Register Function
    if choice == 1:
        print("Registration Page Under Development Process...")
    
    # calling Login Function
    elif choice == 2:
        account = int(input("Enter Your Account Number:"))
        password = input("Enter your password:")
        login_val = login(account=account, password=password)
        
        while login_val:
            print("The Small Scale Bank Providing Services")
            print("1. Balance \n 2. Withdraw \n 3. Deposit \n \
                4. Transfer \n 5. Ministatement \n 6. Logout")
            choice = int(input("Enter Your Choice(1-6):"))
            
            if choice == 1:
                #call Balance Function
                current_balance = balance(account=account)
                print(f"Current Balance is:{current_balance}")
                
            elif choice == 2:
                amount=int(input("Enter your withdraw amount:"))
                # call Withdraw Function
                res = withdraw(account=account, withdraw_amount=amount)
                print(res)
                
            elif choice == 3:
                amount=int(input("Enter your deposit amount:"))
                # call Deposit Function
                res = deposit(account=account, deposit_amount=amount)
                print(res)
            
            elif choice == 4:
                amount = int(input("Enter your Transfer amount:"))
                receiver_account = int(input("Enter Receiver Account Number:"))
                # call Transfer Function
                res = transfer(sender=account, reciever=receiver_account, transfer_amount=amount)
                print(res)
                
            elif choice == 5:
                #call Ministatement Function
                res = ministatement(account=account)
                print(res)
            
            elif choice == 6:
                # call Logout Function
                print(logout())
                exit()
                
            else:
                print("Invalid choice, select in between 1-6")
        print("Invalid Login Credentials")  
    else:
        print("Invalid choice, select in between 1 and 2")