# super() gives you access to methods in a superclass
# from the subclass that inherits from it

# super() alone returns a temporary object of the superclass
#  that then allows you to call that superclass’s methods.


class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length, **kwargs):
        # super is used to reference the parent object(superclass)
        # "Rectangle" from said reference is then called the
        #  __init__ passing length as both necessary arguments
        #  needed to initialize the parent

        # super() can also take two parameters: the first is the subclass,
        # and the second parameter is an object that is an instance of that
        # subclass.

        # In Python 3, the super(Square, self) call is equivalent to the
        # parameterless super() call. The first parameter refers to the
        # subclass Square, while the second parameter refers to a Square
        #  object which, in this case, is self.

        # super() can be called with other classes as well
        super().__init__(length=length, width=length, **kwargs)


class VolumeMixin:
    # There’s exist technique that can help  get around the complexity of
    # multiple inheritance while still providing many of the benefits. This technique
    # is in the form of a specialized, simple class called a mixin

    # A mixin works as a kind of inheritance, but instead of defining an “is-a”
    # relationship it may be more accurate to say that it defines an “includes-a”
    # relationship. With a mix-in you can write a behavior that can be directly
    # included in any number of other classes
    def volume(self):
        return self.area() * self.height


class Cube(VolumeMixin, Square):

    # "The parameterless call to super() is recommended and sufficient
    # for most use cases, and needing to change the search hierarchy
    # regularly could be indicative of a larger design issue"

    # By including an instantiated object, super() returns a bound method:
    # a method that is bound to the object, which gives the method the
    # object’s context such as any instance attributes. If this parameter
    # is not included, the method returned is just a function,
    # unassociated with an object’s context

    # Technically, super() doesn’t return a method. It returns a proxy
    # object. This is an object that delegates calls to the correct class
    # methods without making an additional object in order to do so.

    def __init__(self, length):
        super().__init__(length)
        self.height = length

    def face_area(self):
        # Setting Square as the subclass argument here causes
        # super to look one stage above the instance hierarchy
        # for the method area(), in this case it will find it in
        # Rectangle
        face_area = super(Square, self).area()
        return face_area

    def surface_area(self):
        # In the example above and the current one calling
        # super with a subclass & instance arguments does
        # nothing but in the case where Square also implemented
        # it's own area/volume() method it'd be useful to specify
        # where exactly you'd want to call the method from
        face_area = super(Square, self).area()
        return face_area * 6


# While the examples above (and below) call super() without any
# parameters, super() can also take two parameters: the first is
# the subclass, and the second parameter is an object that is an
# instance of that subclass.

# cube = Cube(3)
# print(cube.surface_area())
# print(cube.volume())

# Multiple Inheritance Overview
# In addition to single inheritance, Python supports multiple inheritance,
# in which a subclass can inherit from multiple superclasses that don’t
#  necessarily inherit from each other (also known as sibling classes).


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        # This will allow users of these objects to instantiate
        # them only with the arguments that make sense for that
        # particular object.
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        # Makes a call to the contructor of Square
        # and passes RightPyramid as an instance along with
        # it's base attribute as argument needed to initialize
        # Square: super(Square, self).__init__(self.base)
        super().__init__(base=base, **kwargs)

    def area(self):
        # "There’s still a problem here: Trianlge & Square
        #  both implement the area() method. This causes
        # issues with the MRO, because the first
        # instance of .area() that is encountered in the
        # MRO list will be called."

        # This can be easily solved by designing classes
        # with unique methods either by name or parameter
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area


pyramid = RightPyramid(base=2, slant_height=4)

# This line will result in an error due to the way
# the Method Resolution Order works it will instead
# call Triangle's implementation of area() pyramid.area()
# however by changing the MRO as specified by
# RightPyramid(Square, Triangle) we can look towards Square for
# our desired method first
print(pyramid.area())
print(pyramid.area_2())

# Method Resolution Order
# The method resolution order (or MRO) tells Python how to search for
# inherited methods. This comes in handy when you’re using super()
# because the MRO tells you exactly where Python will look for a method
# you’re calling with super() and in what order

# Every class has an .__mro__ attribute that allows us to inspect the order,
# this can be done as such:
# print(RightPyramid.__mro__)
# This tells us that methods will be searched first in Rightpyramid,
# then in Triangle, then in Square, then Rectangle, and then, if nothing
# is found, in object, from which all classes originate from.
