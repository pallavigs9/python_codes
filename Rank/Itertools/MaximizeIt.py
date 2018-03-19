'''
IP
3 1000
2 5 4        <-- Max value 5
3 7 8 9      <-- Max value 9
5 5 7 8 9 10 <-- Max value 10
OP
206
Exp
So 5
'''
from itertools import product

k, m = map(int, raw_input().split())
ip_list = []
result_lst = []

for i in range(k):
    list_arr = [int(n)*int(n) for n in raw_input('').split()]
    ip_list.append(list_arr)

prod_list = list(product(*ip_list))
uni_list = set(prod_list)
for arr in uni_list:
    max_no = reduce(lambda x, y: x + y, arr) % m
    result_lst.append(max_no)

print max(result_lst)
'''
6 767
2 488512261 423332742
2 625040505 443232774
1 4553600
4 92134264 617699202 124100179 337650738
2 778493847 932097163
5 489894997 496724555 693361712 935903331 518538304

763
'''

