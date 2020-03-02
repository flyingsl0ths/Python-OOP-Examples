# Python Object-Oriented Programming: Class Variables


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


emp_1 = Employee("Flying", "Sloths", 50000, "someemail123@somewhere.com")
emp_2 = Employee("Test", "User", 50000, "testemail321@somewhere.com")

## Accessing methods that use class variables ##
# print(f"Before applying raise: {emp_1.pay}")

# emp_1.ApplyRaise()

# print(f"After applying 4% raise: {emp_1.pay}")
################################################

## Accessing class variables ##
# Employee.raise_amount = 1.05
# When accessing a class variable using an instance
# python checks if the instance contains that attribute as such
# using the __dict__ attribute which returns a dictionary or other mapping object
# used to store an object’s (writable) attributes.
# print(emp_1.__dict__)

# if not then python checks the inheriting class for said attribute
# print(Employee.__dict__)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
###############################

## NameSpace ##

# Creates a variable within the namespace of the instance
# This is entirely different than using the object itself to
# perform the global assigment, as explained in the previous block
# This is the same as creating an new field within the emp_1 instance
# As oppose to this: Employee.raise_amount = 1.05 which sets the value
# for all instances of Employee again explained in the previous block
# emp_1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(emp_1.__dict__)

# Increments the class variable num_employees by 1 each time
# a new instance is created
# print(Employee.num_of_employees)

# Accessing the num_of_employees class variable
# print(emp_1.num_of_employees)
################
