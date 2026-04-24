import time

def main_system():
    print("-" * 50)
    print("WELLCOME TO ELLAF-FASHION MASTER SYSTEM")
    print("-" * 50)
    
    # Project 2: Password Logic (Security System)
    
    admin_password = "admin123"
    user_input = input("Enter the admin password to access the system: ")
    if user_input != admin_password:
        print("Access Denied! Incorrect password.")
        time.sleep(0.10)
        return
    print("\n Access Granted! Welcome to the system.")
    
    while True:
        print("\n" + "-" * 50)
        print("MAIN DASHBOARD")
        print("-" * 50)
        print("1. Wholesale and Retail Management System (proj 2)")
        print("2. Student Grading system (proj 3)")
        print("3. Student Result Management System (proj 4)")
        print("4. Real Calculator (proj 5)")
        print("5. Even or Odd Checker (proj 6)")
        print("6. Exit")
        choice = input("\n Enter your choice (1-6): ")
        if not choice.isdigit() or not 1 <= int(choice) <= 6:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
        # --- OPTION 1. WHOLESALE AND RETAIL MANAGEMENT SYSTEM (proj 2) ---
        
        if choice == '1':
            try:
                quantity = int(input("Enter the quantity of items: "))
                price_per_item = float(input("Enter the price per item: "))
                total_cost = quantity * price_per_item
                if quantity >= 12:
                    price_per_item = 1500
                    discount = 0.10 * total_cost
                    total_cost -= discount
                    print(f"Wholesale price after 10% discount: {total_cost:.2f}")
                elif quantity >= 6:
                    price_per_item = 2000
                    discount = 0.05 * total_cost
                    total_cost -= discount
                    print(f"Retail price after 5% discount: {total_cost:.2f}")
                else:
                    price_per_item = 2500
                    print(f"Retail price: {total_cost:.2f}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                
        # --- OPTION 1. Complete Than Move To Option 2 ---
         # --- OPTION 2. Student Grading System (proj 3) ---
         
        elif choice == "2":
            try:
                total = total_cost
                if total >= 15000:
                    customer_type = "Premium Customer"
                elif total >= 10000:
                    customer_type = "Regular Customer"
                else:
                    customer_type = "Happy Customer"
                print(f"Customer Type: {customer_type}")
            except NameError:
                print("Please perform a calculation in option 1 before checking customer type.")
                
                # --- OPTION 2. Complete Than Move To Option 3 ---
                # --- OPTION 3. Delivery Management System (proj 4) ---
                
        elif choice == "3":
            city = input("Enter the city for delivery: ").lower()
            weight = float(input("Enter the weight of the package (in kg): "))
            try:
                if city == "karachi":
                    cost = 250
                elif city == "lahore":
                    cost = 200
                elif city == "islamabad":
                    cost = 150
                else:
                    cost = 300
                    
                # --- Weight of Option 3. Complete Than Move To Option 4 --- 
                
                if weight >= 5:
                    cost += 100
                print(f"Extra Weight Charge: {100 if weight >= 5 else 0}")
                print(f"Total delivery cost for {weight} kg to {city.title()}: {cost:.2f}")
            except ValueError:
                print("Invalid input. Please enter a numeric value for weight.")
                
        # --- OPTION 4. Real Calculator (proj 5) ---
        # --- OPTION 4. Complete Than Move To Option 5 ---
        
        elif choice == "4": 
            def real_calculator():
                print("Welcome to the Real Calculator!")
                print("You can perform addition, subtraction, multiplication, and division.")
                
                while True:
                    try:
                        num1 = float(input("Enter the first number: "))
                        operator = input("Enter the operator (+, -, *, /): ")
                        num2 = float(input("Enter the second number: "))
                        
                        if operator == '+':
                            result = num1 + num2
                        elif operator == '-':
                            result = num1 - num2
                        elif operator == '*':
                            result = num1 * num2
                        elif operator == '/':
                            if num2 != 0:
                                result = num1 / num2
                            else:
                                print("Error: Division by zero is not allowed.")
                                continue
                        else:
                            print("Invalid operator. Please try again.")
                            continue
                        
                        print(f"The result of {num1} {operator} {num2} is: {result}")
                    
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                    
                    cont = input("Do you want to perform another calculation? (yes/no): ")
                    if cont.lower() != 'yes':
                        print("Thank you for using the Real Calculator. Goodbye!")
                        break
                    
            real_calculator()
            
        # --- OPTION 5. Even or Odd Checker (proj 6) ---
        
        elif choice == "5":
            def check_even_odd():
                print("Welcome to the Even or Odd Checker for Project 6!")
                try:
                    units = int(input("Enter the number of units: "))
                    if units % 2 != 0:
                        print(f"Warning: {units} Stock Incomplete Pair Missing")
                    else:
                        print(f"{units} Stock is Complete.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                
            check_even_odd()
            
        # --- OPTION 6. Exit ---
        
        elif choice == "6":
            print("Thank you for using the ELLAF-FASHION MASTER SYSTEM. Goodbye!")
            break
main_system()