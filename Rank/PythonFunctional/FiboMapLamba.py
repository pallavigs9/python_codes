'''Python Functionals > Map and lambda Print Cubes of Fibonaccies Series Of A Given number 
I/P 5
O/P [0, 1, 1, 8, 27]'''
user = int(raw_input(''))
def fibo(no):
    fib = []
    a = 0
    b = 1
    fib.append(a)
    fib.append(b)

    for i in range(no - 2):
        c = a + b
        fib.append(c)
        a = b
        b = c
    return fib

if user == 0:
    print '[]'
elif user == 1:
    print '[0]'
else:
    tp = map(lambda x: x ** 3, fibo(user))
    print tp