def find(n):
    n = n + 1
    return sum([i for i in range(3,n) if i%3 == 0 or i%5 == 0])

print find(5)
print find(90560)