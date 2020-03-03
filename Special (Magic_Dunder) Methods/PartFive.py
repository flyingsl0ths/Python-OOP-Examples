# Python Object-Oriented Programming: Special(Magic/Dunder) Methods


class Employee(object):
    # self is the first argument a class always takes
    # self refers to the instance of said object
    # self is used for accessing fields or methods(functions)
    # within a class

    # Class variables are fields that are shared amongst
    # every instance of said class they can be accessed via the
    # Class itself or the instance Employee.raise_amount/self.raise_amount
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay, email):
        # The initialiser method/ contructor, __init__ for short
        # is the blueprint for what variables/fielemp_2ds every instance
        # of said object must be passed to it before it can be created
        # this is alot more efficient than doing it manually
        # as noted below
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = email

    def FullName(self):
        # Methods must also take self as the first argument
        # in order to know which object to operate on, they
        # can be accessed without self as well
        return "{} {}".format(self.first_name, self.last_name)

    def ApplyRaise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)

    # These two methods must always be implemented
    def __repr__(self):
        # Meant to be used as an unambigous representation
        # of an object meant to be used for debugging purposes
        # A rule of thumb for this is to return something that can
        # be used to recreate the object itself in python
        return f"Employee({self.first_name}, {self.last_name}, {self.pay}, {self.email})"

    def __str__(self):
        # Meant to be used for as a readable form
        # of the object for the end user
        # without an implemented __repr__ method calling __str__
        # on an object will return __repr__ as a fallback
        return f"{self.FullName()}: {self.email}"

    def __add__(self, other):
        # Implmented version of __add__ depicts how addition
        # is performed on two objects of the type Employee
        # Using NotImplemented is a way of falling back on another object
        # to see if they know how to handle the error else an error is 
        # thrown eventually
        return self.pay + other.pay if isinstance(other, Employee) else NotImplemented

    def __len__(self):
        # Implemented version of __len__ depicts the length
        # of an Employee objects full name as returned via FullName()
        return len(self.FullName())

emp_1 = Employee("Flying", "Sloths", 50000, "testEmail321@somewhere.com")
emp_2 = Employee("Test", "Employee", 50000, "testEmail110@somewhere.com")

#print(emp_1)

# __repr__ & __str__ can be directly called
# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# __add__ depicts how data types should be performed addition on
# print(1 + 2)
# print(int.__add__(1, 2))

# String objects use their own version of __add__
# print(str.__add__('a', 'b'))

# Implmented version of __add__ to perform addition on two Employee object
# print(emp_1 + emp_2)

# len() function accesses a dunder method __len__ when used on an object
# print(len("test"))
# print("test".__len__())
#  print(len(emp_1))