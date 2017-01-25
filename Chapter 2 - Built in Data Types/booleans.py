print int(True)     # True behaves like 1
print int(False)    # False behaves like 0
print bool(1)       # 1 evaluates to True in a boolean context
print bool(-42)     # and so does a every non zero number
print bool(0)       # 0 evaluates to False

# quick peak at the operators (and, or, not)
print not True
print not False
print True and True
print False or True

print 1 + True
print False + 42
print 7 - True

# Reals
pi = 3.1415926536
radius = 4.5
area = pi * (radius ** 2)
print area

import sys
print sys.float_info
