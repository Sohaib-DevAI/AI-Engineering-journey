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
        select_option = input("\n1. Withdraw, 2. Deposit, 3. Exit, 4. PIN Change.")
        print(select_option)
        # 1. Withdraw option
        if select_option == "1":
            withdraw_amount = int(input("Enter amount to withdraw: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"Transaction Successful! New Balance : Rs {balance}")
            else:
                print("Insufficient Balance!")
        # 2. Deposit option
        elif select_option == "2":
            deposit_amount = int(input("Enter amount to deposit: "))
            balance += deposit_amount
            print(f"Deposit Successful! New Balance: Rs {balance}")
        # 3. Eixt option 
        elif select_option == "3":
            print("=" * 50)
            print("Thank you for using Rendom Digital Banking System.")
            print("=" * 50)
            print("Please collect your card")
            print("=" * 50)
            break
        # 4. PIN Change Option
        elif select_option == "4":
            current_pin_check = input("Enter your OLD 4-digit PIN: ")
            
            if current_pin_check == actual_pin:
                new_pin = input("Enter your NEW 4-digit PIN: ")
                confirm_pin = input("Confirm your NEW 4-digit PIN: ")
                
                if new_pin == confirm_pin:
                    actual_pin = new_pin  # variable update 
                    print("PIN Changed Successfully! Please use the new PIN next time.")
                else:
                    print("PIN Mismatch! Both entries must be same.")
            else:
                print("Incorrect Old PIN! Cannot change PIN.")
        else:
            print("Invalid Option! Please select 1-4.")
            continue # Wapas options par le jayega
        
        # --- Professional Receipt System  ---
        print("\n" + "="*50)
        show_receipt = input("Do you want to print a transaction receipt? (yes/no): ").lower()
        
        if show_receipt == "yes":
            import datetime
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print("\n" + "*" * 50)
            print(f"{'OFFICIAL TRANSACTION RECEIPT':^50}")
            print("*" * 50)
            print(f"Date & Time   : {current_time}")
            print(f"Customer Name : Sohaib Khan")
            print(f"Account No.   : XXXX-XXXX-4521")
            print(f"Bank Branch   : AI-Engineering Digital")
            print("-" * 50)
            print(f"Status        : SUCCESSFUL")
            print(f"Final Balance : Rs {balance:,}.00")
            print("-" * 50)
            print(f"{'KEEP THIS RECEIPT FOR YOUR RECORDS':^50}")
            print("*" * 50)
            print("\nTransaction Complete. Have a nice day!")
        else:
            print("\nNo receipt printed. Thank you for saving paper!")

        break # one Transaction than loop stop

# out of loop
if attempts == 0:
    print("\n" + "!"*50)
    print("CRITICAL ERROR: Too many incorrect PIN attempts.")
    print("Your account has been temporarily locked.")
    print("Please visit the nearest branch with your CNIC.")
    print("!"*50)