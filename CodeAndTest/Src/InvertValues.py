'''Return inverse no from list. Each positive becomes negatives, and the negatives become positives.'''

def invert(lst):
    new_lst = []
    for no in lst:
        new_lst.append(-no)
    return new_lst

print invert([])

'''
Clevar Soluation would be
return [-x for x in lst]'''