S = input()
S = S.replace('BC', 'D')

cnt = 0
ans = 0
for i, s in enumerate(S):
    if s == 'D':
        ans += cnt
    elif s == 'A':
        cnt += 1
    else:
        cnt = 0
print(ans)
