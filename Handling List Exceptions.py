def replace_artist(top_artists):
    try:
        # Ask the user for the index of the artist to replace
        index = int(input("Enter the index of the artist you want to replace (1-10): ")) - int(1)
        # Ask for the new artist name
        new_artist = input("Enter the new artist name: ").strip()
        # Replace the artist at the specified index
        top_artists[index] = new_artist
        print(f"Artist at index {index} has been replaced with {new_artist}.")
    except (ValueError, IndexError):
        # Handle both ValueError and IndexError in a single except block
        print("An input error occurred.")
def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Display the current list of top artists
    print("Current list of top artists:")
    for i in range(len(top_artists)):
        print(f"{i+1}: {top_artists[i]}")  # No enumerate used
    # Call the function to replace an artist
    replace_artist(top_artists)
    # Display the updated list
    print("\nUpdated list of top artists:")
    for i in range(len(top_artists)):
        print(f"{i+1}: {top_artists[i]}")
main()