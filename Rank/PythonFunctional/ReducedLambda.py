'''Soluation my way'''
from fractions import Fraction

userIp = int(raw_input(''))
Frac = 1/1
for i in range(userIp):
    n, d = map(str, raw_input('').split())
    Frac = Fraction(Frac) * Fraction(int(n), int(d))

print Frac.numerator, Frac.denominator

'''Solution other way'''
def product(fracs):
    t = reduce(lambda x,y : x*y,fracs)
    return t.numerator, t.denominator