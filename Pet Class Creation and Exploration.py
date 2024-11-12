#create pet class
class Pet:
    #create constructor
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name
    #define get methods
    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
    
    def get_name(self):
        return self.__name
    #define set methods
    def set_kind(self, kind):
        self.__kind = kind

    def set_breed(self, breed):
        self._breed = breed
    
    def set_name(self, name):
        self.__name = name
    #define print details method
    def print_details(self):
        print(f"Pet Details:\nKind: {self.__kind}\nBreed: {self.__breed}\nName: {self.__name}\n")
#create 3 instances of pets
pet1 = Pet("Parrot", "Cockatiel", "Chip")
pet2 = Pet("Dog", "German Shepard", "Dogmeat")
pet3 = Pet("Fish", "Piranha", "Chomp")
#print pet details
pet1.print_details()
pet2.print_details()
pet3.print_details()
#get attribute special function
print("Breed of pet3:", getattr(pet3, "_Pet__breed"))