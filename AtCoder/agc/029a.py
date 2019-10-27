S = input()

ans = 0
right = 0

for i, s in enumerate(S[:: -1]):
    if s == 'B':
        ans += i - right
        right += 1

print(ans)