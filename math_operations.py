import numpy as np 

def add(a, b):
    return a + b


def substract(a, b):
    print(
        "this function is used to the numbers a and b and add them together. Then it will return the results"
    )
    return a - b


def multiply(a, b):
    return a * b


def mean(numbers):
    return np.mean(numbers)

numbers = [1,2,3]
print(mean(numbers))
