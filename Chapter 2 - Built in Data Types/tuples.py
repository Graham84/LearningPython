t = ()      # empty tuple
print type(t)
one_element_tuple = (42, )      # you need the comma
print one_element_tuple
three_element_tuple = (1, 3, 5)
print three_element_tuple

a, b, c = 1, 2, 3               # tuple for multiple assignment
print a, b, c                   # implicit tuple with one instruction

print 3 in three_element_tuple  # membership test


# traditional way of swapping values
a, b = 1, 2
c = a                           # we need three lines and a temporary var c
a = b
b = c
print a, b                      # a and b have been swapped

# python way of swapping values
a, b = b, a                     # this is the Pythonic way to do it
print a, b
