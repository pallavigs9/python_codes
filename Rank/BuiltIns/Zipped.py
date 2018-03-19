students, lines = map(str, raw_input('').split())
MarkLst = []
for ln in range(int(lines)):
    ip = [float(n) for n in raw_input('').split()]
    if len(ip) == int(students):
        MarkLst.append(ip)

ZipMark = zip(*MarkLst)
for i in ZipMark:
    ave = sum(i) / len(i)
    print "%.1f" % ave


'''Print the averages of all students on separate lines.
5 3
I/P
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
O/P
90.0 
91.0 
82.0 
90.0 
85.5 '''