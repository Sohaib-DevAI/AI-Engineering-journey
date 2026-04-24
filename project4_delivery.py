def calculate_delivery():
# Delivery cost calculation based on city
    print("The Lubaba Luxury Delivery System")
    city = input("Enter the (city) name: ")
    weight = int(input("Enter the weight of the item in kg: "))
    if city == "karachi":
        cost = 200
    elif city == "lahore":
        cost = 150
    elif city == "islamabad":
        cost = 100
    else:
        cost = 250
        # Delivery cost base on weight
    if weight >= 5:
        cost = cost + 100
    print(f"Additional cost for weight is > 5 kg: 100 PKR")
    print(f"Total shipping cost is {cost} PKR")

calculate_delivery()