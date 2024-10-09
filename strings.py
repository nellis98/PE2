def main():
    # Example string
    example_string = "Hello, Python programmers!"
    #Iterate through the string and print each character
    print("Iterating through the string:")
    for character in example_string:
        print(character)
    #Find and print the character with the minimum ASCII value in the string
    minimum = min(example_string)
    print(f"\nCharacter with the minimum ASCII value: {minimum}")
    #Find and print the character with the maximum ASCII value in the string
    maximum = max(example_string)
    print(f"\nCharacter with the maximum ASCII value: {maximum}")
    #Find and print the index of the first occurrence of 'o' in the string
    index_of_o = example_string.index("o")
    print(f"\nIndex of 'o': {index_of_o}")
    #Convert the string into a list of characters and print the list
    example_list = list(example_string)
    print(f"\nConverting string to a list of characters: {example_list}")
    #Count and print the number of occurrences of 'o' in the string
    count_of_o = example_string.count("o")
    print(f"\nCount of 'o' in the string: {count_of_o}")
main()
