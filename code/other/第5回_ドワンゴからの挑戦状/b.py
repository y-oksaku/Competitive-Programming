import re

S = input()

S = S.replace('25', '#')
S = re.sub(r'[0-9]', ' ', S)
S = S.split()

ans = 0
for s in S:
    ans += len(s) * (len(s) + 1) // 2

print(ans)