N = int(input())
A = list(map(int, input().split()))

ans = 0
for i, a in enumerate(A):
    a -= 1
    if A[a] - 1 == i:
        ans += 1
print(ans // 2)
