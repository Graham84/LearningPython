from fractions import Fraction
x = Fraction(10, 6)                     # notice its been reduced to lowest terms 5/3
print x
y = Fraction(1, 3) + Fraction(2, 3)     # 1/3 + 2/3 = 3/3 = 1/1
print y
z = Fraction(10, 6)
print z.numerator                       # 5
print z.denominator                     # 3

from decimal import Decimal as D        # rename for brevity
print D(3.14)                           # pi, from float, so approximation issues
print D('3.14')                         # pi, from a string, so no approximation issues
print D(0.1) * D(3) - D(0.3)            # from float we still have the issue
print D('0.1') * D('3') - D('0.3')      # from string all perfect

