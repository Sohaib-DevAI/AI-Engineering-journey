#======================
#PROJECT ATM SIMULATOR
#======================

print("=" * 50)
print(f"{'RENDOM DIGITAL BANKING SYSTEM':^50}")
print("=" * 50)

#Initial Setup
actual_pin = "1234"
balance = 50000  # Initial Balance
attempts = 3

while attempts > 0:
    user_pin = input(f"\nPlease enter your 4-digit pin ({attempts} attempts left): ")
    
    if user_pin == actual_pin:
        print("\nPIN Verified Successfully!")
        print("\nSelect Option 1-3")
        select_option = input("\n1. Withdraw, 2. Deposit, 3. Exit.")
        print(select_option)
        if select_option == "1":
            withdraw_amount = int(input("Enter amount to withdraw: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"Transaction Successful! New Balance : Rs {balance}")
            else:
                print("Insufficient Balance!")
        elif select_option == "2":
            deposit_amount = int(input("Enter amount to deposit: "))
            balance += deposit_amount
            print(f"Deposit Successful! New Balance: Rs {balance}")
        elif select_option == "3":
            print("Thank you for using Rendom Digital Banking System.")
            break
        else:
            print("Invalid Option! Try Again.")
            break
        
            
                
            
    