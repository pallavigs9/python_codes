def square_digit(num):
    new_num = ''
    for i in str(num):
        new_num = new_num + str((int(i) * int(i)))
    return int(new_num)

print square_digit(9119)



