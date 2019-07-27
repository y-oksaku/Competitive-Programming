N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N - 1, -1, -1) :
    left = min(A[i + 1], B[i])
    ans += left
    B[i] -= left
    center = min(A[i], B[i])
    ans += center
    A[i] -= center

print(ans)