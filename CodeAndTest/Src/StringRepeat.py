'''Ip 2 abc
OP abcabc'''

def repeat_str(repeat, string):
    return ''.join(string for i in range(repeat))


print repeat_str(5, "Hello ")


