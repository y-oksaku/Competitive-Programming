N, A, B = map(int, input().split())
ans = []
a = 0
b = 0
c = 0
for i, s in enumerate(input()):
    if s == 'a':
        if a + b < A + B:
            ans.append('Yes')
            a += 1
        else:
            ans.append('No')
    if s == 'b':
        if a + b < A + B and c < B:
            ans.append('Yes')
            b += 1
        else:
            ans.append('No')
        c += 1
    if s == 'c':
        ans.append('No')

print(*ans, sep='\n')
