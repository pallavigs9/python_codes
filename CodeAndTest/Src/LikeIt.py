def likes(names_lst):

    if len(names_lst) == 0:
        print 'no one likes this'
    elif len(names_lst) == 1:
        first = map(str, names_lst)
        print '{} likes this'.format(first)
    elif len(names_lst) == 2:
        first, second = map(str,names_lst)
        print '{} and {} like this'.format(first, second)
    elif len(names_lst) == 3:
        first, second, third = map(str, names_lst)
        print '{}, {} and {} like this'.format(first, second, third)
    elif len(names_lst) >= 4:
        first = names_lst[0]
        second = names_lst[1]
        all_len = len(names_lst) - 2
        print '{}, {} and {} others like this'.format(first, second, all_len)

likes([])