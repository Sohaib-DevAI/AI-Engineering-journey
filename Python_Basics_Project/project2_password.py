# PASSWORD CKECKER FOR LUBABA LUXURY
import time

    
print(
      "Welcome to Lubaba Luxury! Please enter the password to access our exclusive services."
    )

secrat_password = "LUBABA_LUXURY"
attempts = 3

def check_password():
    global attempts

    while attempts > 0:
        user_input = input("Enter the password: ")
        if user_input == secrat_password:
            print("Access granted! Welcome to Lubaba Luxury.")
            return
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
    print("Access denied! You have exhausted all attempts. Please try again later.")
    if attempts == 0:
        print("\n Please wait 5 seconds...")
        time.sleep(5)
        print("You can try again now.")
        attempts = 3
        check_password()


check_password()
