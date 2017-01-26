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