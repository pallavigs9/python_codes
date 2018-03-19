'''Find which one of the given number differs from other numbers and return index of that number'''

def iq(numbers):
    index = 1
    numLst = [int(n) for n in numbers.split()]
    evennums = [no for no in numLst if no % 2 == 0]
    oddnums = [num for num in numLst if num % 2 != 0]
    if len(evennums) == 1:
        print 'In Even'
        for i in numLst:
            if i == evennums:
                break
            else:
                index = index + 1
    elif len(oddnums) == 1:
        print 'In Odd'
        for i in numLst:
            if i == oddnums[0]:
                break
            else:
                index = index + 1
    return index


print iq('1 2 1 1')