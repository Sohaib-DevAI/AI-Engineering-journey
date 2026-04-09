# PROJECT 1 - LUBABA LUXURY WHOLESALE CUSTOMERS
print("=" * 50)
print("Welcome to LUBABA LUXURY WHOLESALE")
print("=" * 50)

quantity = int(input("Enter the quantity of items: "))

# logic one check karna ki inventory zero se kam to nahi hai
if quantity < 0:
    print("Invalid quantity. Please enter a non-negative number.")
else:
    # logic two wholsale vs ratail price check karna
    if quantity >= 12:
        rate = 1500
        print("LUBABA LUXURY WHOLESALE AFTER 12 SUITS PRICE 1500")
    elif quantity >= 7:
        rate = 1700
        print("LUBABA LUXURY WHOLESALE AFTER 7 SUITS PRICE 1700")
    else:
        rate = 2000
        print("LUBABA LUXURY WHOLESALE FOR LESS THAN 3 SUITS PRICE 2000")

    # logic three agar total cost 30000 se zeyada ho to 5% discount dena
    total_cost = quantity * rate
    if total_cost > 30000:
        discount = total_cost * 0.05
        total_cost -= discount
        print("-" * 50)
        print("Congratulations! You got a 5% discount on your total cost.")
        print("=" * 50)
        print(f"Discount: RS {discount}")
        print("-" * 50)
    print(f"Total cost: RS {total_cost}")
    print("Thank you for shopping with LUBABA LUXURY WHOLESALE! Have a great day!")
        
