#define pet class
class Pet:
    #define class variable
    vet_name = "Huntley Veterinary Hospital"
    #define the constuctor
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type = "Dog"):
        #define instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type
    #define get functions
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type
    #define set functions
    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value
    #define display function
    def display_pet_info(self):
        print(f"\n{self.__owner_first_name} \n{self.__owner_last_name} \n{self.__pet_id} \n{self.__pet_name} \n{self.__pet_type}")
#create 3 instances  
Pet1 = Pet("Nate", "Ellis", "453", "Bella", "Cat")
Pet2 = Pet("Jessica", "Pompi", "232", "Finn", "Dog")
Pet3 = Pet("Brian", "Bauer", "875", "Chomp", "Guinea pig")
#display info
Pet1.display_pet_info()
Pet2.display_pet_info()
Pet3.display_pet_info()
#set info
Pet1.set_owner_first_name("Nathan")
Pet1.set_pet_name("Bellatrix")
Pet1.set_pet_id("563")
Pet2.set_owner_last_name("Pompei")
Pet3.set_pet_type("Gerbal")
#write check property function
def check_property(pet, property_name):
    if hasattr(pet, property_name) == True:
        print(f"Property '{property_name}' exists in the Pet object")
    else:
        print(f"Property '{property_name}' does not exist in the Pet object.")
#display info
Pet1.display_pet_info()
Pet2.display_pet_info()
Pet3.display_pet_info()
#check property
check_property(Pet1, "get_owner_first_name")
check_property(Pet1, "get_owner_last_name")
check_property(Pet2, "get_pet_id")
check_property(Pet3, "get_pet_name")
check_property(Pet3, "get_pet_type")