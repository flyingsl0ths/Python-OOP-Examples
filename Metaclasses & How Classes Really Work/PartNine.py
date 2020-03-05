# def hello():
    # A class is an object even though a class
    # can create objects as well 
    # (an object is data that can be manipulated)
    # class Hi:
    #     pass

    # return Hi

# Meta classes define the rules for class
# Classes define the the rules for an object

# When a class is created a metaclass is used for it's 
# creation, this all happens automatically

# class Test:
    # When a class is created the constructor of
    # the metaclass 'type' is called to make the object itself
    # pass

# Using the 'type' constructor manually to creates a class
# using the given arguments: 
# name(internal representation for the class),
# any bases(anything inherited from),
# and any attributes

# Manually creating an object using type()
# class Foo:
    # When using the class keyword all rules defined for
    # the object created are passed to the constructor
    # type() of the metaclass and the object is created
#     def show(self):
#         print("hi")

# def add_attrs(self):
#     self.z = 9

# Test = type('Test', (Foo,), {"x": 5, "add_attribute": add_attrs})

# Instantiating an instance works the same way
# t = Test()

# Adding attributes works the same way
# t.y = "hello"
# print(t.y)

# Calling methods works the same way
# t.show()
# t.add_attribute()
# print(t.z)

# Everything objects do is the same using type()
# instead of class for instantiating an object
##################

## Inheriting from a metaclass
# class Meta(type):
#     def __new__(self, class_name, bases, attrs):
        # __new__() is a dunder method
        # that is always called before __init__()
        # it can be used to hook into & modifie an objects
        # creation

        # Example: Changing all attributes to uppercase
        # a = {}
        # for name, val in attrs.items():
        #     if name.startswith("__"):
        #         a[name] = val
        #     else:
        #         a[name.upper()] = val

        # return type(class_name, bases, a)


# class Dog(metaclass=Meta):
    # The default metaclass is type
    # metaclass can be passed a new metaclass
    # and use the behavior defined in that metaclass
    
    # x = 5
    # y = 8

    # def hello(self):
    #     print("hello")


# d = Dog()

# print(d.X)
# d.HELLO()