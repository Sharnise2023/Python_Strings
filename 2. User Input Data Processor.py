# Task 1:
def validate_name_length():
    # Ask for user's first name
    first_name = input("Enter your first name: ")
    # check the length of the first name
    if len(first_name) < 2:
        print("Error: First name must be at least 2 characters long.")
        return
    #Ask for user's last name
    last_name = input("Enter your last name: ")
    if len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")
        return
    print(f"Hello, {first_name} {last_name}! Your name has been sucessfully validated.")

validate_name_length()