#create the not numeric error class
class NotNumericError(Exception):
    "Exception raised by non-numeric input"
    pass
#define the function
def enter_user_input():
    #create a loop
    while True:
        #use try block
        try:
            #accept user input
            user_input = input("Please enter a number: ")
            #if not numeric raise error
            if not user_input.isnumeric():
                raise NotNumericError("The input is not numeric. ")
        #except block using as e
        except NotNumericError as e:
            print(f"error: {e}")
        #else block for valid input
        else:
            print("Thanks! Input Valid.")
            #ends program when valid input is added
            break
        #finally block that always executes
        finally:
            print("End of the program execution.")
#call the function
enter_user_input()
       