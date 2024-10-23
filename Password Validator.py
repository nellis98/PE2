#define function for password requirements
def password_requirements(password):
    #if length is less than 8 or greater than 20 print a message explaining this
    if len(password) < 8 or len(password) > 20:
        print("Password must be between 8 and 20 characters")
    #set variables equal to false
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    #set the symbols available in special symbols
    special_symbols = "!@#$%&*"
    #create a for loop
    for char in password:
        #check for uppercase characters and sets the variable equal to true if there are uppercase characters found
        if char.isupper():
            has_upper = True
        #check for lowercase characters and sets the variable equal to true if there are lowercase characters found
        elif char.islower():
            has_lower = True
        #check for digit characters and sets the variable equal to true if there are digit characters found
        elif char.isdigit():
            has_digit = True
        #check for special characters and sets the variable equal to true if there are special characters found
        elif char in special_symbols:
            has_special = True
    #checks to see if any of the conditions specifically arent met     
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_digit:
        print("Password must contain at least one number.")
    if not has_special:
        print(f"Password must contain at least one special symbol from {special_symbols}.")
    #checks to see that all conditions are met at the same time
    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False
#define a main function
def main():
    #create a while loop
    while True:
        #use try and except statements
        try:
            #ask the user to enter a password
            password = input("Enter a password: ")
            #validate the password
            if password_requirements(password):
                print("Password meets all criteria.")
                #ask for confirmation
                confirm_password = input("Confirm your password: ")
            #check if the passwords match
            if password == confirm_password:
                print("Success! Passwords match.")
                #exit the loop if all checks pass
                break
            else:
                print("Passwords do not match. Please try again.")
        except ValueError:
            print("Value Error")
#call the main function       
main()
