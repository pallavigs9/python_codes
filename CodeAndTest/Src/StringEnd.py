
def solution(string, ending):

    if string[-len(ending):] == ending:
        return True
    else:
        return False

print solution('abcde', 'cde')

'''
One line solution
return string.endswith(ending)'''