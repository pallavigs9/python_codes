import cmath

result = cmath.polar(complex(raw_input('')))
val1, val2 = map(float, result)
print round(val1, 3)
print round(val2, 3)