#define Person Class
class Person:
    #define the constructor
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
    #create a get info function
    def get_info(self):
        return f"\n{self.__name} \n{self.__address} \n{self.__age} \n{self.__phone_number}"
    #create a get name function
    def get_name(self):
        return self.__name
    #create a get address function
    def get_address(self):
        return self.__address
    #create a get age function
    def get_age(self):
        return self.__age
    #create a get phone number function
    def get_phone_number(self):
        return self.__phone_number
    #create a set name function
    def set_name(self, name):
        self.__name = name
    #create a set address function
    def set_address(self, address):
        self.__address = address
    #create a set age function
    def set_age(self, age):
        self.__age = age
    #create a set phone number function
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
#define three objects in the class
Person1 = Person("Nate", "9535 Cummings Street", "26", "2247694506")
Person2 = Person("Jessica", "123 Apple way", "27", "7083012222")
Person3 = Person("Brian", "45678 wild path", "28", "6304557789")
#display information about each object
print(Person1.get_info())
print(Person2.get_info())
print(Person3.get_info())
