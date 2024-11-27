#import datetime from datetime
from datetime import datetime
#define main function
def main():
   #create a space between entries?
    print("\n\n")
    #use try statements to help solve errors
    try:
        #get todays date and time
        today = datetime.today()
        #input birth year
        birth_year = int(input("What year were you born?  "))
        #input birth month
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        #input birth day
        day = int(input("What day of the month were you born?  "))
        #create a datetime object for the user's birthday
        birthday = datetime(birth_year, month, day)
        #print "Your birthday is: "
        print("Your birthday is: ")
        #format the user's birthday as YYYY-MM-DD
        birthday_output = birthday.strftime("%Y-%m-%d")
        #print the user's birthday in its formatted version
        print(birthday_output) 
        #calculate the difference between today and the user's birthday
        delta = today - birthday
        #print the number of days difference it is between today and the user's birthday
        print(f'Difference is {delta.days} days')
        #solve for the number of years by dividing the number of days by 365.2425 days
        delta_years = delta.days // 365.2425
        #print the number of years difference between today and the user's birthday
        print(f'You are {delta_years} years old')
        #solve for the number of months by dividing delta.days by 30.41 days the average numbr of days in a month
        delta_months = delta.days // 30.41
        #print the number of months difference between today and the user's birthday
        print(f'You are {delta_months} months old')
        #solve for the number of weeks by dividing delta.days by 7
        delta_weeks = delta.days // 7
        #print the number of weeks difference between today and the user's birthday
        print(f'You are {delta_weeks} weeks old')
    #use except statements to help solve errors  
    except Exception as e:
        #print a message if there is an error
        print(f"ooooops!!!:  {e}") 
        #call the function if there was an error the first time
        main()
#call the function
main()