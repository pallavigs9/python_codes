'''A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]'''

from itertools import product


def carte_prod():
    finalList = []
    ip1 = raw_input('').split()
    ip2 = raw_input('').split()

    lst1 = list(product(ip1, ip2))
    print lst1
    for i in lst1:
        finalList.append((int(i[0]), int(i[1])))
    for tupal in finalList:
        print tupal,


carte_prod()