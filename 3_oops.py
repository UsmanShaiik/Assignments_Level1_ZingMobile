""" Class Definition (Person):
Initialization:

Initialize the attributes name, age, and mobile to store personal details.
Setting Values:

Define a method set_values to allow the user to input personal details.
Printing Values:

Define a method print_values to print the stored personal details. """
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.mobile = ""
    
    def set_values(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.mobile = input("Enter mobile number: ")
    
    def print_values(self):
        print("\n")
        print("your entered details are:-")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.mobile)

#instance of the Person class
person = Person()

# Setting values by taking input from the user
person.set_values()

# Printing those values using class objects
person.print_values()
