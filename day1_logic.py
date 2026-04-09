# ---LUBABA LUXURY BILLING LOGIC---
print("Welcome to Day 1 :Variables and Data Types")
# 1. Variable (Customer Ka Data Store Karna)
customer_name = input("Enter Customer Name: ")
item_price = float(input("Enter Item Price: "))

# 2. Logic (Condition Check Karna)
# Agar bill 5000 se zyada hai to 10% discount do
if item_price >= 10000:
    discount = item_price * 0.20
    final_bill = item_price - discount
    print(
        f"Congratulations {customer_name}! You got a 20% VIP discount. Your final bill is: {final_bill}"
    )
elif item_price >= 5000:
    discount = item_price * 0.10
    final_bill = item_price - discount
    print(
        f"Congratulations {customer_name}! You got a 10% discount. Your final bill is: {final_bill}"
    )
else:
    discount = 0
    final_bill = item_price
    print(f"Thank you {customer_name}! Your final bill is: {final_bill}")

# 3. Output (Result Show Karna)
print("_" * 30)
print(f"Customer Name: {customer_name}")
print(f"Total Bill: Rs.{item_price}")
print(f"Discount: Rs.{discount}")
print(f"Final Bill: Rs.{final_bill}")
print("Thank you for shopping with Lubaba Luxury! Have a great day!")
