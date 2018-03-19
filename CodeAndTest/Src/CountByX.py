'''
IP (1,10) -> OP [1,2,3,4,5...10]
(2,5)-> [2,4,6,8,10]'''

def count_by(x, n):
    result_lst = []
    cnt = x

    for i in range(1,n+1):
        result_lst.append(cnt)
        cnt = cnt + x
    return result_lst

print count_by(1,5)
print count_by(100,5)


