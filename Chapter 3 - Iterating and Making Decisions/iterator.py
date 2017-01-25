# infinite.py
from __future__ import print_function
from itertools import count
for n in count(5, 3):
    if n > 20:
        break
    print(n, end=', ')          # instead of newline, comma and space


# compress.py
from itertools import compress
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10
even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print('\n',odd_selector)
print(even_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)

# Combinatoric generators
# permutation.py
from itertools import permutations
print(list(permutations('ABC')))
