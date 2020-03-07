import sys

# class Gen:
#     # Generators allow the ability to process large amounts
#     # of data by only keeping the last value processed in memory
#     def __init__(self, n):
#         self.n = n
#         self.last = 0

#     def __next__(self):
#         # Manual implementation of a generator
#         if self.last == self.n:
#             raise StopIteration()

#         rv = self.last ** 2
#         self.last += 1
#         return rv


# g = Gen(100)

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

def gen(n):
    for i in range(n):
        # Yield keyword "yields" whereever it is called
        # from and if called from a function/method/loop
        # pauses said function/method/loop and keeps track
        # of the current state within it such that when its
        # called again the previous state is remembered
        # More than one yield keyword can be used as well
        yield i ** 2


def gen2():
    yield 1
    yield 10
    yield 100
    yield 1000
    yield 10000
    yield 100000


x = [i**2 for i in range(10000)]
g = gen(10000)

print("Number of bytes: ", sys.getsizeof(x))
print("Number of bytes: ", sys.getsizeof(g))

# for i in g:
#     # Calls gen() loops up to last value returned from
#     # gen() n-1 times
#     print(i)

# next() can be used to call functions that yield values as well
# print(next(g))



# StopIteration is raised when exceding amount
# of values yielded us reached
# g2 = gen2()
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))

# When accessing a previous yielded value a segmentation fault
# may occur this is due to the way generators work by accessing
# a previous value twice we are really just accessing a memory
# location that we no longer have accesss to i.e SegmentationFault