sent = '2*4/2+1-1' # result should be 4
sent2 = '11+2*3'
equ_lst = ' '.join(sent2).split()

while len(equ_lst) > 1:
    if '*' in equ_lst:
        rightNo = equ_lst[equ_lst.index('*') + 1]
        leftNo = equ_lst[equ_lst.index('*') - 1]
        multi = int(rightNo) * int(leftNo)
        print multi
        idx1 = equ_lst.index('*')
        equ_lst[idx1] = multi
        equ_lst.remove(rightNo)
        equ_lst.remove(leftNo)

    elif '/' in equ_lst:
        rightNo = equ_lst[equ_lst.index('/') + 1]
        leftNo = equ_lst[equ_lst.index('/') - 1]
        if int(rightNo) > int(leftNo):
            divi = int(rightNo) / int(leftNo)
        else:
            divi = int(leftNo) / int(rightNo)
        print divi
        idx2 = equ_lst.index('/')    #4
        equ_lst[idx2] = divi
        equ_lst.remove(rightNo)
        equ_lst.remove(leftNo)

    elif '+' in equ_lst:
        rightNo = equ_lst[equ_lst.index('+') + 1]
        leftNo = equ_lst[equ_lst.index('+') - 1]
        add = int(rightNo) + int(leftNo)
        print add
        idx3 = equ_lst.index('+')
        equ_lst[idx3] = add
        equ_lst.remove(rightNo)
        equ_lst.remove(leftNo)

    elif '-' in equ_lst:
        rightNo = equ_lst[equ_lst.index('-') + 1]
        leftNo = equ_lst[equ_lst.index('-') - 1]

        if int(rightNo) > int(leftNo):
            minus = int(rightNo) - int(leftNo)
        else:
            minus = int(leftNo) - int(rightNo)
        print minus
        idx4 = equ_lst.index('-')
        equ_lst[idx4] = minus
        equ_lst.remove(rightNo)
        equ_lst.remove(leftNo)

print equ_lst