def password_requirements(password):
    if len(password) < 8 or len(password) > 20:
        print("Password must be between 8 and 20 characters")
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_symbols = "!@#$%&*"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_symbols:
            has_special = True
            
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_digit:
        print("Password must contain at least one number.")
    if not has_special:
        print(f"Password must contain at least one special symbol from {special_symbols}.")
    
    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False

def main():
    while True:
        try:
            # Ask the user to enter a password
            password = input("Enter a password: ")

            # Validate the password
            if password_requirements(password):
                print("Password meets all criteria.")
                # Ask for confirmation
                confirm_password = input("Confirm your password: ")

            # Check if the passwords match
            if password == confirm_password:
                print("Success! Passwords match.")
                break  # Exit the loop if all checks pass
            else:
                print("Passwords do not match. Please try again.")
        except ValueError:
            print("Value Error")
        
main()