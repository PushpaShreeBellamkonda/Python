def decorator1(f):
    def inner():
        print("before calling the function")
        f()
        print("after calling the function")
    return inner

@decorator1
def greet():
    print("hello pushpa")
greet()



'''
1. Function Decorators:
The most common type of decorator, which takes a function as input and returns a new function. The example above demonstrates this type.
'''