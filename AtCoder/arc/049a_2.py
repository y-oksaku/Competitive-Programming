S = input() + '\0'
A, B, C, D = map(int, input().split())

ans = ''
for i, s in enumerate(S):
    if i in [A, B, C, D]:
        ans += '"'
    ans += s

print(ans.replace('\0', ''))