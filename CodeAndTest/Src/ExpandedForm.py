def expanded_form(num):
    num = str(num)
    new_str = ''
    index = 0
    for i in num:
        if i == '0':
            index = index + 1
        else:
            add_zero = num[index+1:]
            new_str = new_str + i
            for z in add_zero:
                new_str = new_str + '0'
            new_str = new_str + ' + '
            index = index + 1
    return new_str[0:-3]

print expanded_form(70304)
