import operator
count = {}
str_ip = raw_input('').strip()
tp = [','.join(i) for i in str_ip]
for k in tp:
    count[k] = count.get(k,0) - 1

line_count = 0
sorted_count = sorted(count.items(), key=operator.itemgetter(1, 0), reverse=False)

for i, j in sorted_count:
    if line_count >= 3:
        break

    print i, abs(j)
    line_count = line_count + 1

'''
Failed Test
Ip qwertyuiopasdfghjklzxcvbnm
OP
a 1
b 1
c 1
'''