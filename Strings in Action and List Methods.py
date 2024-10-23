#define main function
def main():
    #create an empty list to store the titles
    book_titles = []
    #create a variable for the counter
    count = 0
    #create a for loop that runs until count hits 10
    while count < 10:
        #accept user input
        title = input(f"Enter book title {count+1}: ")
        #append the capitalized titles to the list
        book_titles.append(title.title())
        #increase the count by one with every iteration
        count += 1
    #sort the list into alphabetical order
    sorted_list = sorted(book_titles)
    #print the sorted list book for book using a for loop
    print("Sorted list of book titles: ")
    for book in sorted_list:
        print(book)
main()