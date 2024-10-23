#define a function to replace an artist
def replace_artist(top_artists):
    #use try and except statements
    try:
        # Ask the user for the index of the artist to replace
        index = int(input("Enter the index of the artist you want to replace (1-10): ")) - int(1)
        # Ask for the new artist name
        new_artist = input("Enter the new artist name: ").strip()
        # Replace the artist at the specified index
        top_artists[index] = new_artist
        #print a message stating that the artist has been replaced
        print(f"Artist at index {index} has been replaced with {new_artist}.")
     # Handle both ValueError and IndexError in a single except block
    except (ValueError, IndexError):
        print("An input error occurred.")
#define the main function
def main():
    #create a list of the top artists
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Display the current list of top artists
    print("Current list of top artists:")
    for i in range(len(top_artists)):
        print(f"{i+1}: {top_artists[i]}")
    # Call the function to replace an artist
    replace_artist(top_artists)
    # Display the updated list
    print("\nUpdated list of top artists:")
    for i in range(len(top_artists)):
        print(f"{i+1}: {top_artists[i]}")
#call the main function
main()