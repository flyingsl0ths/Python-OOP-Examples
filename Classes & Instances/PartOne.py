# Python Object-Oriented Programming: Creating/Instanciating A Class


class Employee(object):
    # self is the first argument a class always takes
    # self refers to the instance of said object
    # self is used for accessing fields or methods(functions) within a class

    def __init__(self, first_name, last_name, pay, email):
        # The initialiser method/ contructor, __init__ for short
        # is the blueprint for what variables/fields every instance
        # of said object must be passed to it before it can be created
        # this is alot more efficient than doing it manually as noted below
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = email

    def FullName(self):
        # Methods must also take self as the first argument
        # in order to know which object to operate on, they
        # can be accessed without self as well
        return "{} {}".format(self.first_name, self.last_name)


#### Manually Assignning Fields To An Object ###
# emp_1.first_name = "Flying"
# emp_1.last_name = "Sloths"
# emp_1.email = "someemail123@somewhere.com"
# emp_1.pay = 50000

# emp_2.first_name = "Test"
# emp_2.last_name = "Tester"
# emp_2.email = "testemail321@somewhere.com"
# emp_2.pay = 50000

# print(emp_1.email +" " + emp_2.email)
################################################

emp_1 = Employee("Flying", "Sloths", 5000, "someemail123@somewhere.com")
emp_2 = Employee("Test", "User", 50000, "testemail321@somewhere.com")

# Example of methods being accessed directly via the class itself
# by passing an instance as an argument to self this is a longer
# notation of what's happening in the next example
print("Self is not know")
print(Employee.FullName(emp_1), end="\n\n")

# Here self is know which is why it is not passed as an argument
# self is the instance emp_1/2
print("Self is known")
print(emp_1.email)
print(emp_2.email, end="\n\n")
print(emp_1.FullName())
print(emp_2.FullName())
