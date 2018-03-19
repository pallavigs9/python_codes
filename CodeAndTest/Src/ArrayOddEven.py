
def Odd_Or_Even(array):
    if sum(array) % 2 == 0:
        return 'even'
    else:
        return 'odd'

print Odd_Or_Even([1023, 1, 2])
print Odd_Or_Even([0, 1, 2])

'''
One line solution 
return 'even' if sum(arr) % 2 == 0 else 'odd''''