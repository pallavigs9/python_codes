def remove_9(number, digit):
    num2 = ''
    for i, n in enumerate(number):
        if (n == digit):
            first7 = i - 1
            last7 = i + 1

            #print "pbs ", first7, " l ", last7


            if number[first7] == '7' and number[last7] == '7' and first7 > 0:
                continue

        num2 = num2 + n
    return num2

print remove_9('9797', '9')
