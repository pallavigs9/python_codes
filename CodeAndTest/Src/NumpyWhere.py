'''from a given list sort odd numbers, without changing even numbers idx'''
import numpy as np

def find_even_idx(num_lst):
    np_lst = np.array(num_lst)
    even_idx = np.where(np_lst % 2 == 0)
    neat_lst = " ".join(map(str, even_idx))
    even_idx_lst = []
    for n in neat_lst:
        if n.isdigit():
            even_idx_lst.append(int(n))
    return even_idx_lst

def sort_odds(num_lst):
    odd_num = [n for n in num_lst if n % 2 != 0]
    odd_num.sort()
    even_num = [n for n in num_lst if n % 2 == 0]
    even_idx = find_even_idx(num_lst)
    for idx, no in zip(even_idx, even_num):
        odd_num.insert(idx, no)

    return odd_num

arr1 = [5, 2, 7, 3, 6]
print sort_odds(arr1)
