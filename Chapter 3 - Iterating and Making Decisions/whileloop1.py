n = 39
remainders = []
while n > 0:
    remainder = n % 2               # remainder of division by 2
    remainders.append(remainder)    # we keep track of remainders
    n //= 2                         # we divide n by 2
# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)


print 39 % 2
print 19.5 % 2
print 9.75 % 2
print 4.75 % 2
print 2.4375 % 2
print 1.21875 % 2


n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)
# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)
