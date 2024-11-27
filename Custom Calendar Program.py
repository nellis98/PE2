#import calendar module
import calendar
#import datetime module
import datetime
#define main function
def main():
    #get the current year
    current_year = datetime.datetime.now().year
    #create a loop
    while True:
        #use try statement to help test for errors
        try:
            #accept user input for their birth month
            birth_month = int(input("Please enter your birth month (1-12): "))
            #if their input is between 1 and 12 break
            if 1 <= birth_month <= 12:
                break
            #otherwise print a statement about bad input
            else:
                print("Invalid input.Please enter a number between 1 and 12.")
        #if there is a value error print this statement
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 12.")
        #if there is an unexpected error print this statement
        except:
            print("Error")
    #print the calendar of their birth month
    print(calendar.month(current_year, birth_month))
#call the main function
main()