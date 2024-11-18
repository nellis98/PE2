#define main function
def main():
    #accept input for date and time
    date_time = input("Enter the date and time (format DD-MM-YYYY HH:MM): ")
    #accpet input for the diary entry
    diary_entry = input("Write your diary entry: ")
    #open the text fine Diary.txt in append mode
    file = open("C:\\Users\\natee\\Python\\8\\Diary\\Diary.txt", "a")
    #write the date and time
    file.write(f"Date and Time: {date_time}\n")
    #write the diary entry
    file.write(f"Dairy Entry: {diary_entry}\n")
    #add a space between entries
    file.write("\n")
    #close the file
    file.close()
#call the main function
main()