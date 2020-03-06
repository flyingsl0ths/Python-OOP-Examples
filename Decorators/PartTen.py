# Decorators allow us to add extra functionality to an existing function

import time


def func(f):
    # This is possible due to functions being
    # objects in python

    # Whenever a decorator function is created
    # the function being used as a decorator must
    # take in a parameter that is a function and the
    # it must be called within said function
    def wrapper(*args, **kwargs):
        # *args, **kwargs can be used to handle when a function
        # using a decorator takes in n aguments
        # or no arguments at all
        print("Started")
        rv = f(*args, **kwargs)
        # A value can also be return in the case that the function
        # using the decorator also returns a value
        print("Ended")
        return rv  # wrapper returns rv

    return wrapper  # func returns whatever wrapper returns


@func
def func2(x, y):
    print(x, y)
    return y

# Equivalent of func3 = func(func3)
# more than one decorator can be used
@func
def func3():
    print("I am Func3")

# x = func("hello")
# x()

# x = func(func2)
# y = func(func3)
# x()
# y()

# Using func3 as a variable we can assign it the
# value of calling func with func3 as an argument
# this is the equivalent of using decorator syntax @function_name
# func3 = func(func3)
# func2 = func(func2)
# func3()
# func2()

# x = func2(5, 6)
# print(x)
# print()

# func3()


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         total = time.time() - start
#         print(f"Time: {total}")

#     return wrapper


# @timer
# def test():
#     for _ in range(1000000):
#         pass


# @timer
# def test2():
#     time.sleep(2)


# test()
# test2()

# Example of using a dcorartor to validate a form
def validate(f):
    def wrapper(*args, **kwargs):
        data = f(*args, **kwargs)
        for key, value in data.items():
            if value != "":
                print(key + ": " + value)
            else:
                print(key + ": empty")

    return wrapper


@validate
def validated_form(form_data):
    return form_data


form = validated_form({"name": "User", "last_name": "Random", 
                       "email": "testEmail321@email.com", "address": ""})

print(form)
