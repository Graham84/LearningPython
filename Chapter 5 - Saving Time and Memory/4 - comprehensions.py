# squares.map.py
# If you code like this you are not a Python guy! ;)

squares = []
for n in range(10):
    squares.append(n ** 2)
print list(squares)

# This is better, one line, nice and readable
squares = map(lambda n: n**2, range(10))
print list(squares)


# squares.comprehension.py
print [n ** 2 for n in range(10)]


# even.squares.py
# using map and filter
sq1 = list(
    filter(lambda n: not n % 2, map(lambda n: n ** 2, range(10)))
)

# equivalent, but using list comprehensions
sq2 = [n ** 2 for n in range(10) if not n % 2]

print(sq1, sq1 == sq2)                          # prints: [0, 4, 16, 36, 64] True


# Nested Comprehensions
# pairs.for.loop.py
items = 'ABCDE'
pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))

print pairs

# pairs.list.comprehension.py
items = 'ABCDE'
pairs = [(items[a], items[b])
    for a in range(len(items)) for b in range(a, len(items))]
print pairs


# pythagorean.triple.py
from math import sqrt
# this will generate all possible pairs
mx = 10
legs = [(a, b, sqrt(a**2 + b**2))
    for a in range(1, mx) for b in range(a, mx)]
# this will filter out all non pythagorean triples
legs = list(
    filter(lambda triple: triple[2].is_integer(), legs))
print(legs)                     # prints: [(3, 4, 5.0), (6, 8, 10.0)]


# pythagorean.triple.int.py
from math import sqrt
mx = 10
legs = [(a, b, sqrt(a**2 + b**2))
    for a in range(1, mx) for b in range(a, mx)]
legs = filter(lambda triple: triple[2].is_integer(), legs)
# this will make the third number in the tuples integer
legs = list(
    map(lambda triple: triple[:2] + (int(triple[2]), ), legs))
print(legs)                     # prints: [(3, 4, 5), (6, 8, 10)]


# pythagorean.triple.comprehension.py
from math import sqrt
# this step is the same as before
mx = 10
legs = [(a, b, sqrt(a**2 + b**2))
    for a in range(1, mx) for b in range(a, mx)]
# here we combine filter and map in one CLEAN list comprehension
legs = [(a, b, int(c)) for a, b, c in legs if c.is_integer()]
print(legs)                      # prints: [(3, 4, 5), (6, 8, 10)]


# dictionary.comprehensions.py
from string import ascii_lowercase
lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print lettermap
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print lettermap


# dictionary.comprehensions.duplicates.py
word = 'Hello'
swaps = {c: c.swapcase() for c in word}
print(swaps)            # prints: {'o': 'O', 'l': 'L', 'e': 'E', 'H': 'h'}


# dictionary.comprehensions.positions.py
word = 'Hello'
positions = {c: k for k, c in enumerate(word)}
print(positions)        # prints: {'l': 3, 'o': 4, 'e': 1, 'H': 0}


# set.comprehensions.py
word = 'Hello'
letters1 = set(c for c in word)
letters2 = {c for c in word}
print(letters1)                     # prints: {'l', 'o', 'H', 'e'}
print(letters1 == letters2)         # prints: True
