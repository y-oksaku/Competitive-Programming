N = int(input())

M = 0
ans = 'No'

for _ in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        M += 1
        if M >= 3:
            ans = 'Yes'
    else:
        M = 0

print(ans)
