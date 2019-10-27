S = input()
S = S.replace('BC', 'D').replace('B', ' ').replace('C', ' ').split()

ans = 0
for s in S:
    leftA = 0
    for i, t in enumerate(s[:: -1]):
        if t == 'A':
            ans += max(0, i - leftA)
            leftA += 1

print(ans)