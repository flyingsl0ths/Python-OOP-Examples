# Python Object-Oriented Programming: Property Decorators - Getters, Setters, and Deleters

import random


class Employee(object):
    # self is the first argument a class always takes
    # self refers to the instance of said object
    # self is used for accessing fields or methods(functions) within a class

    def __init__(self, first_name, last_name):
        # The initialiser method/ contructor, __init__ for short
        # is the blueprint for what variables/fields every instance
        # of said object must be passed to it before it can be created
        # this is alot more efficient than doing it manually as noted below
        self.first_name = first_name
        self.last_name = last_name

    @property
    # Allows the use of methods as class fields
    def email(self):
        return "{}{}{}@email.com".format(self.first_name, self.last_name, str(random.randint(0, 100)))

    @property
    def FullName(self):
        # Methods must also take self as the first argument
        # in order to know which object to operate on, they
        # can be accessed without self as well
        return "{} {}".format(self.first_name, self.last_name)

    @FullName.setter
    # Allows a given method with a property decorator
    # to accepted arguments sytanx is as follows
    # @method_name.setter
    def FullName(self, name):
        self.first_name, self.last_name = name.split(' ')

    @FullName.deleter
    # Allows a given method with a property decorator
    # to "delete" class fields via "del" keyword
    # @method_name.deleter
    def FullName(self):
        print("Deleted Name")
        self.first_name, self.last_name = None, None


emp_1 = Employee("John", "Smith")

emp_1.FullName = "Jim Smith"

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.FullName)

del emp_1.FullName

print(emp_1.FullName)
