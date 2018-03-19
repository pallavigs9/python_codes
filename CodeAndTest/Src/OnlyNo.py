'''From list of non-negative integers and strings,
returns a new list with the strings filtered out.(means only nums)'''

def filter_nos(lst):
    new_lst = []
    for no in lst:
        if str(no).isdigit() and int(no) not in new_lst:
            new_lst.append(int(no))
    return new_lst

print filter_nos([1,2,'aasf','1','123',123])
print filter_nos([1,'a','b',0,15])
print filter_nos([1])