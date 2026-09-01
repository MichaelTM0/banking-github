# ------------------------------------------
# Banking Simulator
# Author: Michael Murchie
#
# Features:
# - User login authentication
# - View checking and savings balances
# - Deposit money
# - Withdraw money
# - Transfer money between accounts
# - View transaction history
# - Input validation for deposits and withdrawals
#
# Version: 1.0
# ------------------------------------------
title = input("Welcome to your bank!")
user = input("Please enter correct Username: ").title()
password = input("Please enter the correct Password: ")

correct_user = "Michael2025"
correct_pass = "HurleyBurley"
checking = 1100.00
savings = 5500.00

transaction_history = []

def transfer():
    global checking, savings
    
    print("\n" + "-"*40)
    print("          TRANSFER MONEY")
    print("-"*40)
    print("1. Checking to savings")
    print("2. Savings to checking")
    print()
    
    option = input("Please choose a number: ")
    amount = float(input("Please enter your transfer amount: "))
    
    
    if option == "1":
        if amount > checking:
            print("Insuffcient Funds!")
        else:
            checking -= amount
            savings += amount
            print("Transfer complete!")
            transaction_history.append(f"Transferred ${amount:.2f} from checking to savings")
            
    elif option == "2":
        if amount > savings:
            print("Insuffcient funds!")
        else:
            savings -= amount
            checking += amount
            print("Transfer complete! ")
            transaction_history.append(f"Transferred ${amount:.2f} from savings to checking")
    else:
        print("\nInvalid option!")
        
            
        
    

if user == correct_user and password == correct_pass:
    print("Login Successfull")

    while True:
        print("\n" + "="*50)
        print("                 BANKING MENU")
        print("1. View Balances")
        print("2. Deposits")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction history")
        print("6. Exit")
        print("-"*50)
    
        action = input("Which feature would you like to use? ").strip().lower()
    
        if action in["1", "view", "balances", "view balances"]:
            print(f"Checking account current balance ${checking:.2f}")
            print(f"Savings account current balance ${savings:.2f}")
            print()
        
        elif action in["2", "deposits", "deposit"]:
            account = input("Are we depositing into checking or savings today? ").lower()
        
            if account == "checking":
                newfunds = float(input("How much are we depositing today? "))
                if newfunds <= 0:
                    print("please enter a positive amount!")
                else:
                    checking += newfunds
                    transaction_history.append(f"Deposited: + ${newfunds:.2f} into checking")
                    print(f"Sucessfully depositied ${newfunds:.2f} into your checking account!")
                    print()
            elif account == "savings":
                newsave = float(input("How much are we depositing into savings today? "))
                if newsave <= 0:
                    print("Please enter a positive amount!")
                else:
                    savings += newsave
                    transaction_history.append(f"Deposited: + ${newsave:.2f} into savings")
                    print(f"Successfully deposited ${newsave:.2f} into your savings account!")
                    print()
            else:
                print("Invalid account option!")
            
        elif action in["3", "withdraw", "withdaws"]:
            a1 = input("Which account are we withdraing from today? ").lower()
        
            if a1 == "checking":
                lessfunds = float(input("how much would you like to withdraw today? "))
                if lessfunds <= 0:
                    print("Please enter a positive amount! ")
                elif lessfunds > checking:
                    print("Insuffiecent Funds!")
                else:
                    checking -= lessfunds
                    transaction_history.append(f"Withdrew - ${lessfunds:.2f} from checking")
                    print(f"Successfully withdrew ${lessfunds:.2f} from your checking account!")
                    print()
                
            elif a1 == "savings":
                lesssave = float(input("How much are we withdrawing from your savings today? "))
                if lesssave <= 0:
                    print("Please enter a positive amount! ")
                elif lesssave > savings:
                    print("Insufficient Funds!")
                else:
                    savings -= lesssave
                    transaction_history.append(f"Withdrew - ${lesssave:.2f} from savings")
                    print(f"You have successfully withdrawn ${lesssave:.2f} from your savings account!")
                    print()
            else:
                print("Invalid option!")
            
        elif action in["4", "transfer", "transfers"]:
            transfer()
            print()
                                       
                                       
        elif action in["5", "transaction history", "transactions", "history", "transaction"]:
            print("Transaction hisotry")
            if transaction_history:
                for trans in transaction_history:
                    print(trans)
            else:
                print("No transactions yet!")

        elif action in["6", "exit", "exits"]:
            print("Thank you for banking with us! Goodbye!")
            break
    
        else:
            print("Invalid choice! Please try again.")
            
else:
    print("Invalid login credentials!")
        
   
        
                       
        
        
        
    