# return.none.py
def func():
    pass

func()              # the return of this call won't be collected. It's lost.
a = func()          # the return of this one instead is collected into `a`
print(a)            # prints: None


# return.single.value.py
def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result

f5 = factorial(5)       # f5 = 120
print f5


# return.single.value.2.py
from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n + 1), 1)
f5 = factorial(5)       # f5 = 120
print f5


# return.multiple.py
def moddiv(a, b):
   return a // b, a % b
print(moddiv(20, 7))    # prints (2, 6)


# side effects
numbers = [4, 1, 7, 5]
print numbers
print sorted(numbers)   # won't sort the original 'numbers' list
print numbers           # lets verify
numbers.sort()          # this will act on the list
print numbers


# recursive.factorial.py
def factorial(n):
    if n in (0, 1):             # base case
        return 1
    return factorial(n - 1) * n     # recursive case


# Anonymous functions
# filter.regular.py
def is_multiple_of_five(n):
    return not n % 5
def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))
print(get_multiples_of_five(50))


# filter.lambda.py
def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))
print(get_multiples_of_five(50))


# lambda.explained.py
# example 1: adder
def adder(a, b):
    return a + b
# is equivalent to:
adder_lambda = lambda a, b: a + b
# example 2: to uppercase
def to_upper(s):
    return s.upper()
# is equivalent to:
to_upper_lambda = lambda s: s.upper()
