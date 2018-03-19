StrIp = raw_input('')

def Alphanum(strng):
    if strng.isalnum():
        print 'True'
    else:
        print 'False'

def Alpha(strng):
    flag = False
    for a in strng:
        if a.isalpha():
            flag = True
    return flag

def Digit(strng):
    flag = False
    for a in strng:
        if a.isdigit():
            flag = True
    return flag

def Lower(strng):
    flag = False
    for a in strng:
        if a.islower():
            flag = True
    return flag

def Upper(strng):
    flag = False
    for a in strng:
        if a.isupper():
            flag = True
    return flag

Alphanum(StrIp)
print Alpha(StrIp)
print Digit(StrIp)
print Lower(StrIp)
print Upper(StrIp)

'''
Simplest Soluation Using Any()
strng = raw_input()
print any(i.isalnum()  for i in strng)
print any(i.isalpha() for i in strng)
print any(i.isdigit() for i in strng)
print any(i.islower() for i in strng)
print any(i.isupper() for i in strng)
'''
