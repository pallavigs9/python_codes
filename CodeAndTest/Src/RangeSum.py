#find the sum of all the numbers between given 2 numbers including them too and return it.

def get_sum(a,b):
    if a > b:
        return sum(range(b, a + 1))
    else:
        return sum(range(a,b + 1))

print get_sum(1,0)
print get_sum(0,-1)
print get_sum(-1,2)

