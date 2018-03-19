#Sucessfully run
import cmath

result = cmath.polar(complex(raw_input('')))
val1, val2 = map(float, result)
print round(val1, 3)
print round(val2, 3)

'''
Test Case Failed
ip -80+25j
OP 83.8152730712
2.83870778521'''