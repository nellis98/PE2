#define the function
def main():
    #create a list
    flower_list = []
    #print information explaining what to enter and how to end the loop
    print("Enter the names of flowers (type 'done' when finished) ")
    #create a loop
    while True:
        #accept user input
        flower = input("Enter flower name: ").strip()
        #if the condition is met break the loop
        if flower.lower() == "done":
            break
        #append the flower names to the list
        flower_list.append(flower)
    #sort the list alphabetically
    flower_list.sort()
    #print statement for the sorted list
    print("Sorted list of flowers: ")
    #add numbers to the list of sorted flowers
    for i in range(len(flower_list)):
        print(f"{i+1} {flower_list[i]}")
    #allow the user to input a flower name
    search_flower = input("Search for a flower by name: ").strip()
    #if the flower is in the list print that it is
    if search_flower in flower_list:
        print(f"{search_flower} is in the list")
    #use try and except statements
    try:
        #search for a flower using the number system
        flower_number = int(input("enter a number associated with a flower: "))
        flower_index = flower_number - 1
        #print the flower with that number
        print(f"The flower at position {flower_number} is: {flower_list[flower_index]}")
    #make an except statement for value error
    except ValueError:
        print("Invalid input. Please enter a number.")
    #make an except statement for index error
    except IndexError:
        print("That number is out of range. Please enter a number between 1 and", len(flower_list))
    #make a generic except statement
    except:
        print("An unexpected error occured.")
#call the function
main()
