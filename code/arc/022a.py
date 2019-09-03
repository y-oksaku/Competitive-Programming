S = input().lower()

seach = ['i', 'c', 't', '!']
pos = 0

for s in S:
    if s == seach[pos]:
        pos += 1

if pos == 3:
    print('YES')
else:
    print('NO')