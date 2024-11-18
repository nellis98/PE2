#import Production Worker class
from Defining_Classes import ProductionWorker
#ask for user input
name = input("Enter the employee's name: ")
number = input("ENter the employee's number: ")
shift_numebr = int(input("Enter the shift number (1 for day, 2 for night): "))
hourly_pay_rate = float(input("Enter the hourly pay rate: "))
#create instance of worker
worker = ProductionWorker(name, number, shift_numebr, hourly_pay_rate)
#print employee details
print("\nEmployee Details:")
print("Name:", worker.get_name())
print("Employee Number:", worker.get_number())
print("Shift Number:", worker.get_shift_number())
print("HOurly Pay Rate:", worker.get_hourly_pay_rate())