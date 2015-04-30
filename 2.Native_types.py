'''
Types
1. Logic
2. Nums
3. Strings
4. Byte
5. Lists [a, b, c, d, a] - not mutable
6. Tuples (a, b, c, d, a) - mutable
7. Unions {a, b, c, d}
8. Dicts {a: b, c: d}
'''

import fractions
import math

def is_it_true(anything):
    return True if anything else False

print('Logical type')
size = 0
print('size is ' + str(size))
print('size < 0: ' + str(size < 0))
print('size > 0: ' + str(size > 0))
print('size == 0: ' + str(size == 0))

print()
print('Nums')
number = 1
print('\tnumber is: ' + str(number))
print("\ttype(number) is " + str(type(number)))
print('\tisinstance(number, int): ', isinstance(number, int))
print('\t1 + 1 = ' + str(1+1))
print('\t1 + 1.0 = ' + str(1+1.0))
print('\ttype(2.0) is ' + str(type(2.0)))
print()

print('Nums convert')
print('\tfloat(2) ' + str(float(2)))
print('\tint(2.0) ' + str(int(2.0)))
print('\tint(2.5) ' + str(int(2.5)))
print('\tint(-2.5) ' + str(int(-2.5)))
print()

print('Op-s')
print('\t11 / 2 = ' + str(11/2))
print('\t11 // 2 = ' + str(11//2))
print('\t-11 // 2 = ' + str(-11//2))
print('\t11.0 / 2 = ' + str(11.0/2))
print('\t11.0 // 2 = ' + str(11.0//2))
print('\t11 ** 2 = ' + str(11**2))
print('\t11 % 2 = ' + str(11%2))
print()

print('Fractials')
x = fractions.Fraction(1,3)
print('\tx = fractions.Fraction(1,3)')
print('\tx = ' + str(x))
print('\tx * 2 = ' + str(x*2))
x = fractions.Fraction(6,4)
print('\tx = fractions.Fraction(6, 4)')
print('\tx = ' + str(x))
try:
    print('\tx = fractions.Fraction(0, 0)')
    x = fractions.Fraction(0,0)
    print('\tx = ' + str(x))
except ZeroDivisionError:
    print('\t\tDiv by 0?!')
print()

print('Geometry')
print('\tpi = ' + str(math.pi))
print('\tsin(pi/2) = ' + str(math.sin(math.pi / 2)))
print('\ttan(pi/4) = ' + str(math.tan(math.pi / 4)))
print()

print('Nums in logical context')
print('\tis_it_true(1): ' + str(is_it_true(1)))
print('\tis_it_true(-1): ' + str(is_it_true(-1)))
print('\tis_it_true(0): ' + str(is_it_true(0)))
print('\tis_it_true(0.1): ' + str(is_it_true(0.1)))
print('\tis_it_true(0.0): ' + str(is_it_true(0.0)))
print('\tis_it_true(fractions.Fraction(1,2)): ' + str(is_it_true(fractions.Fraction(1,2))))
print('\tis_it_true(fractions.Fraction(0,1)): ' + str(is_it_true(fractions.Fraction(0,1))))

