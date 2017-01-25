a = 12
b = 3

print a + b
print b - a
print a // b        # integer division
print a / b         # true division
print a * b
print b ** a        # power operator
print 2 ** 1024     # a very big number, Python handles it gracefully

print 7 / 4         # true division
print 7 // 4        # integer division, flooring returns 1
print -7 / 4        # true division again, result is opposite of previous
print -7 // 4       # integer division, result not the opposite of previous

print int(1.75)
print int(-1.75)

print 10 % 3        # remainder of the division 10 // 3
print 10 % 4        # remainder of the division 10 // 4
