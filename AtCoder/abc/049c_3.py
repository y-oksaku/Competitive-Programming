S = input()
T = ['dream', 'dreamer', 'erase', 'eraser']
T = set([s[::-1] for s in T])

A = ''
for s in S[::-1]:
    A += s
    if A in T:
        A = ''
print('YES' if A == '' else 'NO')