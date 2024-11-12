#create employee superclass
class Employee:
    #create constructor
    def __init__(self, name, number):
        #create attributes
        self.__name = name
        self.__number = number
    #define get functions
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    #define set functions
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number
    
class ProductionWorker(Employee):
    #define constuctor
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        #initialize superclass attributes
        super().__init__(name, number)
        #create attributes
        self.__shift_numebr = shift_number
        self.__hourly_pay_rate = hourly_pay_rate
    #define get functions
    def get_shift_number(self):
        return self.__shift_numebr
    
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
    #define set functions
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate 