#AUTOMATED INVOICE BOT
# BUSSINESS ELLAF FASHION

import datetime

#HEADER DESIGN
print("=" * 60)
print(f"{'ELLAF FASHION INVOICE' :^60}")
print("=" * 60)

#CUSTOMER INFORMATION
customer_name = input("Enter customer name: ")
customer_phone = int(input("Enter customer phone number: "))
date_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#PRODUCT DETAILS (WHOLESALE / RETAIL LOGIC)
print("\n---Available Inventory---")
print("1. Zara Shah Jahan 3pc - Rs 8699 each")
print("2. Mahnoor 3pc - Rs 5899 each")
print("3. Maheen 2pc  - Rs 6399 each")
print("4. Saira 3pc- Rs 4999 each")
print("Local Brand Pakistani Dresses with high quality and affordable prices.Just Rs 4599")
print("\nNote: For wholesale orders (quantity >= 10), a 10% discount will be applied.")
#Input for product selection and quantity
product_choice = int(input("\nEnter the product number (1-4): "))
quantity = int(input("Enter the quantity: "))
#Product price mapping
if product_choice == 1:
    product_name = "Zara Shah Jahan 3pc"
    unit_price = 8699
elif product_choice == 2:
    product_name = "Mahnoor 3pc"
    unit_price = 5899
elif product_choice == 3:
    product_name = "Maheen 2pc"
    unit_price = 6399
elif product_choice == 4:
    product_name = "Saira 3pc"
    unit_price = 4999
else:
    product_name = "Local brand"
    unit_price = 4599
    
#Subtotal calculation and tax application
subtotal = unit_price * quantity
tax_rate = 0.17  # 17% sales tax
tax_amount = subtotal * tax_rate

#Calculate total price and apply discount if applicable
total_price = subtotal + tax_amount
if quantity >= 10:
    discount = total_price * 0.10
    total_price -= discount
else:
    discount = 0
    
#Final invoice generation
print("\n" + "=" * 60)
print(f"{'INVOICE DETAILS' :^60}")
print("=" * 60)
print(f"Customer Name: {customer_name}")
print(f"Phone Number: {customer_phone}")
print(f"Date: {date_today}")
print("-" * 60)

final_bill = total_price
print(f"Final Bill: Rs {final_bill:.2f}")
