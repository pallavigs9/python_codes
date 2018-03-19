'''Perform append, pop, popleft and appendleft methods on an empty deque d.'''

from collections import deque
d = deque()

noofoper = int(raw_input(''))

for i in range(noofoper):
    oper = [str(a) for a in raw_input('').split()]
    method = oper[0]
    if len(oper) > 1:
        value = int(oper[1])
    if (method == 'append'):
        d.append(value)
    elif (method == 'pop'):
        d.pop()
    elif (method == 'popleft'):
        d.popleft()
    elif (method == 'appendleft'):
        d.appendleft(value)

print " ".join(map(str, d))