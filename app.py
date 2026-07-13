

# user table
users = {1234:{'name':'pavan', 'Email':'saip74770@gmail.com', 'balance':5000, 'password':'1234'},
         1235:{'name':'sai', 'Email':'saip74770@gmail.com', 'balance':1000, 'password':'1235'}
        }


# services
def register(name:str, email:str, initial_deposite:int, password:str):
    pass

def login(account:int, password:str)->bool:
    if account in users:
        if password == users[account]['password']:
            print("Login Successfull..\n")
            return True
        else:
            print("Incorrect password..\n")
    else:
        print("Account not number found please register first..\n")
        return False

# balance function defination
def get_balance(account:int)->int:
    curr_amount = users[account]['balance']
    return curr_amount

# withdraw function defination
def withdraw(account:int, withdraw_amt:int)->str:
    curr_amount = users[account]['balance']
    #check amount
    if curr_amount >= withdraw_amt:
        users[account]['balance'] -= withdraw_amt
        return f"{withdraw_amt} withdraw Successfull and \
                    current balance is:{users[account]['balance']}"
    return "Insufficient balance"

# deposit function defination
def deposit(account:int, deposit_amt:int):
    users[account]['balance'] += deposit_amt
    return f"{deposit_amt} deposited Successfull and \
                current balance is:{users[account]['balance']}"

# Transfer function defination
def transfer(sender:int, reciever:int, transfer_amt:int):
    if reciever in users:
        curr_amount = users[sender]['balance']
        if curr_amount >= transfer_amt:
            users[sender]['balance'] -= transfer_amt
            users[reciever]['balance'] += transfer_amt
            return f"{transfer_amt} transfer Successfull and \
                        current balance is:{users[sender]['balance']}"
        return "Insufficient balance"
    return "Reciever account not found"

# Mini statement function defination
def ministatement(account:int):
    print("Your are in mini statement page..")

# logout 
def logout():
    return "Thank you using small scale bank services, Bye Bye..."


# main
if __name__ == "__main__":

    print("Welcome to the small scale bank")
    print("1. Register \n 2.Login")
    choice = int(input("Select your choice:"))

    # calling register function 
    if choice  == 1:
        print("Registation page under development process....")

    # calling login function
    elif choice == 2:
        account = int(input("Enter Your account number:"))
        password = input("Enter your password:")
        login_val = login(account=account, password=password)

        while login_val:
            print("The small scale Bank providing services")
            print("1. Balance \n 2. withdraw \n 3. Deposite \n \
                   4. Transfer \n 5. Ministatement \n 6. Logout")
            choice = int(input("Enter your choice(1-6):"))

            if choice == 1:
                # call Balance function
                current_balance = balance(account=account)
                print(f"Current Balance is:{current_balance}")

            elif choice == 2:
                amount = int(input("Enter your withdraw amount:"))
                # call withdraw function
                res = withdraw(account=account, withdraw_amt=amount)
                print(res)
            
            elif choice == 3:
                amount = int(input("Enter deposit amount: "))
                # call deposit function
                res = deposit(account=account, deposit_amt=amount)
                print(res)

            elif choice == 4:
                receiver = int(input("Enter reciever account number: "))
                amount = int(input("Enter transfer amount: "))
                # call transfer function
                res = transfer(sender=account, reciever=receiver, transfer_amt=amount)
                print(res)

            elif choice == 5:
                # call ministatement function
                res = ministatement(account=account)
                print(res)

            elif choice == 6:
                # call logout function
                login_val = logout()
                exit()

            else:
                print("Invalid Choice, select in between 1-6")

    else:
        print("Invalid Choice, slect in between 1-2")

