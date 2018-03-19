simp_arr = [5, 3, 7]
even_nums = [2, 4, 6]
even_idx = [1, 2, 3]

for idx, n in zip(even_idx, even_nums):
    print idx, n
    simp_arr.insert(idx, n)

print simp_arr

