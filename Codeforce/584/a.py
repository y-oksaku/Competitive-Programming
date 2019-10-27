N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 0

for i, a in enumerate(A):
    for b in A[:i]:
        if a % b == 0:
            break
    else:
        ans += 1

print(ans)
