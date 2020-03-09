from contextlib import contextmanager

# context Managers allow the use of automatic resource handling
# this can be exceptionally useful when working with shared
# resources, shared memory, threads, etc

# "Manual" implementation of a context manager
# file = open(r"Context Managers\file.txt", "r")

# try:
#     file.write("hello")
# finally:
#     print("closing file")
#     file.close()

# Actual implementation of a context manager
# with open(r"Context Managers\file.txt", "w") as file:
# When using the context manager: with followed by a function
# said function instructs "with" what to do at the time of "entering"
# the resource and "exiting" the resouce via __enter__() & __exit__()

# "with" ensures that each instruction within its code block
# is performed regardless of the outcome of previous instructions
# outcomes

# Once the code block used within "with" is finished executing
# the __exit__() method is always called regardless of the outcome
# of the operation

# This comes is useful when working with files
# or unlocking/locking shared memory
# file.write("hello")


# Class Based Implementation of a context manager
# class File:
#     def __init__(self, filename, method):
#         self.file = open(filename, method)

#     def __enter__(self):
#         print("Enter")
#         return self.file

#     def __exit__(self, type, value, traceback):
# Regardless of whether an exception is raised
# __exit__() will be called with these parameters:
# type, value, traceback

# Accessing contents of type, value, traceback
# can be used to look at the "type" of exception
# passed to __exit__ it's "value" and it's
# "traceback" location in memory
# print(f"{type}, {value} {traceback}")

# print("Exit")
# self.file.close()

# If an exception is allowed then True is returned
# althought a better practice would be to specify
# which exceptions to handle using if-statements
# if type == Exception:
#     return True
# Else False is returned and the program is stopped


# with File(r"Context Managers\file.txt", "w") as f:
# Any Exception raised here will automatically
# be passed to __exit__() to see if it will
# be handled
# print("Middle")
# f.write("Hello")

# Using contextlib.contextmanager decorator to transform
# a function into a context manager
# @contextmanager
# def file(filename, method):
#     print("Enter")
#     file = open(filename, method)
#     yield file
#     file.close()
#     print("Exit")
    
    
# with file(r"Context Managers\file.txt", "w") as f:
#     print("Middle")
#     f.write("Hello")