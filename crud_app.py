#define the main function
def main_menu():
    #print menu
    print("Menu:")
    #create a while loop
    while True:
        #use a try statement to help look for errors
        try:
            #print the menu options
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by search term")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            #accept input for the users choice in menu action
            choice = int(input("Please enter the number of your selection: "))
            #if the number given a number 1-5
            if 1 <= choice <= 5:
                #return the choice
                return choice
            #otherwise print that the input is invalid
            else:
                #print a statement about the invalid input
                print("That is not a valid number. Try again.")
        #use an except statement help solve errors
        except ValueError:
            #print a statemment about the value error
            print("That is not a valid number. Try again.")
#define the check function
def check():
    #print checking the system
    print("Checking the system...")
    #use try statements to look for errors
    try:
        #open customer_list.txt in read
        file = open("customer_list.txt", 'r')
        #read the lines of the file
        lines = file.readlines()
        #close the file
        file.close()
        #return the lines
        return lines
    #use except statements to help solve errors
    except FileNotFoundError:
        #print a message about the file not existing
        print("Customer list does not exist. Creating a new file...")
        #create a file by opening the name of the file in write mode
        file = open("customer_list.txt", 'w')
        #close the file
        file.close()
        return []
#define the create function
def create():
    #print creating a new entry
    print("Creating a new entry...")
    #call the check function
    customer = check()
    #accept input for a new entry
    fname = input("Please enter the customer\'s first name: ")
    lname = input("Please enter the customer\'s last name: ")
    phone = input("Please enter the customer\'s phone: ")
    email = input("Please enter the customer\'s email: ")
    #save the input as an entry
    entry = f"{fname}, {lname}, {phone}, {email}\\n"
    #add the entry to the file
    customer.append(entry)
    #save the file
    save(customer)
#define save function
def save(output):
    #open the file in write mode
    file = open("customer_list.txt", 'w')
    #start a for loop
    for line in output:
        #writes the lines of the output into the file
        file.write(line)
    #close the file
    file.close()
    #print a message stating the file has been updated
    print("File updated.")
#define read function
def read():
    #print reading an entry
    print("Reading an entry...")
    #call the check function
    customer_list = check()
    #accept user input for search terms
    search_term = input("Enter the first or last name, phone number, or email of the customer you are searching: ").lower()
    #set the variable found equal to false
    found = False
    #start a for loop
    for line in customer_list:
        #create the variable line_parts from the striped and split lines of customer_list
        line_parts = line.strip().split(", ")
        #save the parts of line_parts as their own variables
        fname = line_parts[0]
        lname = line_parts[1]
        phone = line_parts[2]
        email = line_parts[3]
        #if search term comes up as the lowercase version of fname, lname, or email, or phone
        if search_term in fname.lower() or search_term in lname.lower() or search_term in phone or search_term in email.lower():
            #print found entry and the entry info
            print(f"Found entry: {fname} {lname}, Phone: {phone}, Email: {email}")
            #change found to true
            found = True
    #if not found
    if not found:
        #print no entry found
        print("No entry found.")
#define update function
def update():
    #print updating an entry
    print("Updating an entry...")
    #call the check function
    customer_list = check()
    #accept search terms
    search_term = input("Enter the first or last name, phone number, or email of the customer you are attempting to update: ").lower()
    #set found to false
    found = False
    #start a for loop in the range of the length of the customer list
    for index in range(len(customer_list)):
        #line varibale is set equal to customer_list index
        line = customer_list[index]
        #create the variable line_parts from the striped and split lines of customer_list
        line_parts = line.strip().split(", ")
        #save the parts of line_parts as their own variables
        fname = line_parts[0]
        lname = line_parts[1]
        phone = line_parts[2]
        email = line_parts[3]
        #if search term comes up as the lowercase version of fname, lname, or email, or phone
        if search_term in fname.lower() or search_term in lname.lower() or search_term in phone or search_term in email.lower():
            #set found to true
            found = True
            #print found entry and the entry info
            print(f"Found entry: {fname} {lname}, Phone: {phone}, Email: {email}")
            #print Leave a field blank to keep the current value
            print("Leave a field blank to keep the current value.")
            #accept input for new values
            new_fname = input(f"New first name (current: {fname}): ") or fname
            new_lname = input(f"New last name (current: {lname}): ") or lname
            new_phone = input(f"New phone (current: {phone}): ") or phone
            new_email = input(f"New email (current: {email}): ") or email
            #save the new info to that entry of the list
            customer_list[index] = f"{new_fname}, {new_lname}, {new_phone}, {new_email}\n"
            #open the file in write
            file = open("customer_list.txt", 'w')
            #write the lines from customer list to the file
            file.writelines(customer_list)
            #close the file
            file.close()
            #print entry updated
            print("Entry updated.")
            #break
            break
    #make an if not statement about found being true
    if not found:
        #print no matching entry found
        print("No matching entry found.")
#define the delete function
def delete():
    #print deleting an entry
    print("Deleting an entry...")
    #call the check function
    customer_list = check()
    #accept input for search terms
    search_term = input("Enter the first or last name, phone number, or email of the customer you are attempting to delete: ").lower()
    #set found equal to false
    found = False
    #start a for loop in the range of the length of the customer list
    for index in range(len(customer_list)):
        #line varibale is set equal to customer_list index
        line = customer_list[index]
        #create the variable line_parts from the striped and split lines of customer_list
        line_parts = line.strip().split(", ")
        #save the parts of line_parts as their own variables
        fname = line_parts[0]
        lname = line_parts[1]
        phone = line_parts[2]
        email = line_parts[3]
        #if search term comes up as the lowercase version of fname, lname, or email, or phone
        if search_term in fname.lower() or search_term in lname.lower() or search_term in phone or search_term in email.lower():
            #set found to true
            found = True
            #print found entry and the entry info
            print(f"Found entry: {fname} {lname}, Phone: {phone}, Email: {email}")
            #accept input of yes or no to confirm deletion
            confirm = input("Are you sure you want to delete this entry? (yes/no): ").lower()
            #if confirm equals yes
            if confirm == "yes":
                #delete that entry of the customer list
                del customer_list[index]
                #open file in write
                file = open("customer_list.txt", 'w')
                #write updated customer_list into the file
                file.writelines(customer_list)
                #close the file
                file.close()
                #print entry deleted
                print("Entry deleted.")
                return
            #otherwwise
            else:
                #print deletion canceled
                print("Deletion canceled.")
                return
    #make an if not statement about found being true 
    if not found:
        #print no matching entry found
        print("No matching entry found.")
#create a while loop
while True:
    #call the main function and assigns its return value to choice
    choice = main_menu()
    #if choice is equal to 1
    if choice == 1:
        #call the create function
        create()
    #otherwise if choice is equal to 2
    elif choice == 2:
        #call the read function
        read()
    #otherwise if choice is equal to 3
    elif choice == 3:
        #call the update function
        update()
    #otherwise if choice is equal to 4
    elif choice == 4:
        #call the delete function
        delete()
    #otherwise if choice is equal to 5
    elif choice == 5:
        #print goodbye
        print("Goodbye!")
        #break
        break