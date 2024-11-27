#define generator function
def two_letter_combinations(char_list):
    #use nested loop and a yield to concentrate two characters and give the result
    for char1 in char_list:
        for char2 in char_list:
            yield char1 + char2
#def main fucntion
def main():
    #create a list of 5 characters
    characters = ["w", "q", "p", "t", "n"]
    #print the combinations
    print("Two letter combinations: ")
    for combination in two_letter_combinations(characters):
        print(combination)
#call main function
main()