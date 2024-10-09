#Use the capitalize() method to capitalize the first letter of the string
string1 = "python"
print(string1.capitalize())

#Use the center() method to center the string in a string of specified width
string2 = "python"
print(string2.center(10))

#Use the endswith() method to check if the string ends with a specified substring "on"
string3 = "python"
if string3.endswith("on"):
    print("yes")
else:
    print("no")

#Find the position of "th" in "python" using find
string4 = "python"
print(string4.find("th"))

#Check if "python3" is alphanumeric using isalnum
string5 = "python3"
print(string5.isalnum())

#Check if "python" is alphabetic using isalpha
string6 = "python"
print(string6.isalpha())

#Check if "python" is in lowercase using islower
string7 = "python"
print(string7.islower())

#Check if "   " is all whitespace using isspace
string8 = "   "
print(string8.isspace())

#Check if "PYTHON" is in uppercase using isupper
string9 = "PYTHON"
print(string9.isupper())

#Join ["Python", "is", "fun"] with "-" as separator using the join method
iterable1 = ["Python", "is", "fun"]
separator = "-"
print(separator.join(iterable1))

#Convert "PYTHON" to lowercase using lower
string10 = "PYTHON"
print(string10.lower())

#Remove leading spaces from "  python" using lstrip
string11 = "  python"
print(string11.lstrip())

#Remove trailing spaces from "python  "
string12 = "python  "
print(string12.rstrip())

#Replace "python" with "snake" in "I love python" using replace
string13 = "I love python"
print(string13.replace("python", "snake"))

#Find the highest index of "n" in "python" using rfind
string14 = "python"
print(string14.rfind("n"))

#Split "python-is-fun" at "-" using split
string15 = "python-is-fun"
print(string15.split("-"))

#Check if "python" starts with "py" using startswith
string16 = "python"
print(string16.startswith("py"))

#Remove spaces from "  python  "
string17 = "  python  "
print(string17.strip())

#Swap case of "Python" using swapcase
string18 = "Python"
print(string18.swapcase())

#Convert "python is fun" to title case using title
string19 = "python is fun"
print(string19.title())

#Convert "python" to uppercase using uper
string20 = "python"
print(string20.upper())
