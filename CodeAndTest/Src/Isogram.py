from collections import Counter

def is_isogram(string):
    string = string.lower()
    str_list = ' '.join(string).split()
    char_dict = Counter(map(str, str_list))
    char_count = char_dict.values()
    return all(i == 1 for i in char_count)

print is_isogram("Dermatoglyphics")
print is_isogram("moOse")
print is_isogram("")
print is_isogram("aba")

'''
One line solution
return len(string) == len(set(string.lower()))'''