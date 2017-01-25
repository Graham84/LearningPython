# func.attributes.py
def multiplication(a, b=1):
    """Return a multiplied by b. """
    return a * b

special_attributes = [
"__doc__", "__name__", "__module__",
"__defaults__", "__code__", "__globals__", "__dict__",
"__closure__",
]

for attribute in special_attributes:
    print(attribute, '->', getattr(multiplication, attribute))


# built in functions
import __builtin__
print dir(__builtin__)


# primes.py
from math import sqrt, ceil

def get_primes(n):
    """Calculate a list of primes up to n (included). """
    primelist = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = int(ceil(sqrt(candidate))) # division limit
        for prime in primelist: # we try only the primes
            if prime > root: # no need to check any further
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
        return primelist
