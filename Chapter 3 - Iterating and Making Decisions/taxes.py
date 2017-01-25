income = 10000
income1 = 15000
income2 = 50000
income3 = 100000

if income < 10000:
    tax_coefficient = 0.0        #1
elif income < 30000:
    tax_coefficient = 0.2        #2
elif income < 100000:
    tax_coefficient = 0.35       #3
else:
    tax_coefficient = 0.45       #4

print('I will pay:', income * tax_coefficient, 'in taxes')
print('I will pay:', income1 * tax_coefficient, 'in taxes')
print('I will pay:', income2 * tax_coefficient, 'in taxes')
print('I will pay:', income3 * tax_coefficient, 'in taxes')
