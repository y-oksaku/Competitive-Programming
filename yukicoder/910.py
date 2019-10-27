from collections import Counter

N = int(input())
S = input()

A = []
ans = 0

# 11, 19, 991

for s in S:
    if s == '3' or s == '5' or s == '7':
        ans += 1
    else:
        A.append(s)

one = 0
nine = 0
for s in A:
    if s == '1':
        one += 1
    else:
        if one > 0:
            ans += 1
            one -= 1
        else:
            nine += 1

add = min(nine // 2, one)
ans += add
ans += (one - add) // 2

print(ans)