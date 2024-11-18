#define main function
def main():
    #create total variable
    total = 0.0
    #create count variable
    count = 0
    #use try and except to look for file not found and other errors
    try:
        #open the file in read mode
        file = open("C:\\Users\\natee\\Python\\8\\Processing_Files\\sales_totals.txt", "r")
        #create a loop that reads the lines of the file
        for line in file:
            #use try statements to look for a value error
            try:
                #strip the newline symbol and convert each line to a float
                sale = float(line.strip())
                #add up the total
                total += sale
                #keep a count
                count += 1
                #print the sale
                print(f"Sale: ${sale:,.2f}")
            except ValueError:
                print(f"Error. Invalid data encountered: {line.strip()}")
            #once data has been added
        if count > 0:
            #take the average
            average = total / count
            #print the total sales in dollars
            print(f"\nTotal Sales: ${total:,.2f}")
            #print the number of sales
            print(f"Number of Sales: {count}")
            #print the average cost of each sale in dollars
            print(f"Average Sale: ${average:,.2f}")
            #if no data has been added print this
        else:
            print("No valid sales date found.")
        #close the file
        file.close
    except FileNotFoundError:
        print("Error. The file 'sales totals.txt' was not found.")
    except Exception as e:
        print(f"An unxpected error occured: {e}")
#call the function
main()