from itertools import combinations

string, k = map(str, raw_input('').split())
sorted_string = ''.join(sorted(string))

first_combi = list(combinations(sorted_string, 1))
print_first_combi = map(lambda x:''.join(x), first_combi)
print '\n'.join(map(str, print_first_combi))
second_combi = list(combinations(sorted_string, int(k)))
print_second_combi = map(lambda y:''.join(y), second_combi)
print '\n'.join(map(str, print_second_combi))