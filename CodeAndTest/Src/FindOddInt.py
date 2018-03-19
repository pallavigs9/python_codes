from collections import Counter

def find_it(seq):
    seq_cnt = Counter(map(int, seq))
    for i in seq_cnt:
        if seq_cnt[i] % 2 != 0:
            return i


print find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])