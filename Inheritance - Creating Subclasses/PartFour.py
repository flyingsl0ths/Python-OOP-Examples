# Python Object-Oriented Programming: Inheritance

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
        # is the blueprint for what variables/fields every instance
        # of said object must be passed to it before it can be created
        # this is alot more efficient than doing it manually
        # as noted below
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = email

    def full_name(self):
        # Methods must also take self as the first argument
        # in order to know which object to operate on, they
        # can be accessed without self as well
        return "{} {}".format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)


class Developer(Employee):
    # Even without defining what the Subclass contains thanks to
    # inheritance all attributes/methods are passed along to it
    # Python first looks within the subclass for an __init__ method
    # if it doesn't find one then it looks towards the chain of the
    # inheritance called, The Method Resolution Order until it finds
    # one if it does not then it will look towards the base object
    # all other objects inherit from called builtins.object

    # Class variables altered within the subclass do not imply a change
    # on the parentclass
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, email, progrm_language):
        super().__init__(first_name, last_name, pay, email)
        self.progrm_language = progrm_language
        # Employee.__init__(self, first_name, last_name, pay, email)
        # is valid as well, super() is more convienient when
        # inheritance is multiple


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, email, employees=None):
        super().__init__(first_name, last_name, pay, email)
        # Mutable objects must never be used as parameters
        # their contents are shared amongst objects/method calls
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print("--> " + emp.full_name())


dev_1 = Developer("Flying", "Sloths", 50000,
                  "testemail321@somewhere.com", "C")
dev_2 = Developer("Test", "Employee", 60000,
                  "testemail123@somewhere.com", "Python")

mangr = Manager("Test", "Manager", 90000,
                "testemail1234@somewhere.com", [dev_1])

# Returns true/false whether an object is an instance of a class
# print(isinstance(mangr, Employee))

# Returns true/false whether a class is a subclass of a class
# print(issubclass(Developer, Employee))

# Using help to display the Method Resolution Order
# print(help(Developer))

# Instanciating subclasses using inheritance to define the subclass
# print(dev_1.email)
# print(dev_2.email)

# Class Variables in subclasses do not imply a change
#  on the parent's class variables
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# Using super() to create an entirely new object
# that inherits from a parent object
# print(dev_1.email)
# print(dev_1.progrm_language)

# mangr.add_employee(dev_2)
# mangr.remove_employee(dev_1)

# print(mangr.email)
# mangr.print_employees()
