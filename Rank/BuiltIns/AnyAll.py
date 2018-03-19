Ip = int(raw_input(''))
NumLst = [str(n) for n in raw_input('').split()]
Positive = all(int(i) > 0 for i in NumLst)
def IsPalin(no):
    flag = False
    if no == no[::-1]:
        flag = True
    return flag
if Positive:
    tp = map(IsPalin, NumLst)
    print any(tp)
else:
    tp = map(IsPalin, NumLst)
    print all(tp)
'''
5
12 9 61 5 14
OP
True
Exp:
All Integers must be positive,print False otherwwise
5 and 9 r palindromic integer, Hence Result is True
'''