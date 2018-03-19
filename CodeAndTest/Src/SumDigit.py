#Return sum of the absolute value of each of the number's decimal digits
#IP -10
#OP 1

def sum_digits(number):
    result = 0
    for i in str(number):
        if i.isdigit():
            result = result + int(i)

    return result

print sum_digits(-32)

'''
Shortest Soluation
sum(int(d) for d in str(abs(number)))
'''