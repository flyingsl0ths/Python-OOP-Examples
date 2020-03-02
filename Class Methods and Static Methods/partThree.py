# Python Object-Oriented Programming: classmethods and staticmethods
import datetime


class Employee(object):
    # self is the first argument a class always takes
    # self refers to the instance of said object
    # self is used for accessing fields or methods(functions)
    # within a class

    # Class variables are fields that are shared amongst
    # every instance of said class they can be accessed via the
    # Class itself or the instance Employee.raise_amount/self.raise_amount
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first_name, last_name, pay, email):
        # The initialiser method/ contructor, __init__ for short
        # is the blueprint for what variables/fields every instance
        # of said object must be passed to it before it can be created
        # this is alot more efficient than doing it manually
        # as noted below
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = email
        Employee.num_of_employees += 1

    def FullName(self):
        # Methods must also take self as the first argument
        # in order to know which object to operate on, they
        # can be accessed without self as well
        return "{} {}".format(self.first_name, self.last_name)

    def ApplyRaise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)

    # Transforms a method into a class method.
    @classmethod
    def set_raise_amount(cls, amount):
        # A class method receives the class as implicit first argument,
        # just like an instance method receives the instance(self)
        # the convention for a class method is cls instead of self
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # Example of using a classmethod as an alternative constructor
        # since cls refers to the class and not the instance this method
        # is used to call the constructor of the class to return an new instance
        first_name, last_name, pay, email = emp_str.split('-')
        return cls(first_name, last_name, pay, email)

    @staticmethod
    def is_workday(day):
        # Static methods do not accept an instance/class as their first
        # argument Static methods work much like regular functions
        # Static methods are included within the class only if they have
        # some relation to the class itself
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Flying", "Sloths", 50000, "someemail123@somewhere.com")
emp_2 = Employee("Test", "User", 50000, "testemail321@somewhere.com")

## Using Class Methods ##
# set_raise_amount takes the class as an argument
# due to it being a classmethod (made possible using the
# @classmethod decorator) this is similar to instance methods taking self
# as their first argument

# Same as Employee.raise_amount = 1.05
# Instances can also use class methods as well
# emp_1.set_raise_amount(1.05)
# Employee.set_raise_amount(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Class Methods can also be used as constructors
# emp_str_3 = 'Jane-Doe-90000-testemail2153@email.com'
# emp_3 = Employee.from_string(emp_str_3)
# print(emp_3.FullName())
# print(emp_3.email)
#########################

## Static Methods ##
# A static method is defined as a method that does not access
# the class/instance
# my_date = datetime.date(2020, 2, 28)
# print(Employee.is_workday(my_date))
####################
