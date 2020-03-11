N = int(input())
A = list(map(int, input().split()))
ans = 0

for mid, a in enumerate(A):
    left = 0
    for l in A[:mid]:
        if l < a:
            left += 1
    right = 0
    for r in A[mid + 1:]:
        if r < a:
            right += 1
    ans += left * right
print(ans)