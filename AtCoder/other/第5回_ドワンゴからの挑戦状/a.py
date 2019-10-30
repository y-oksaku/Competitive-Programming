N = int(input())
A = list(map(int, input().split()))
avg = sum(A) / N
ans = 0
for i, a in enumerate(A):
    if abs(A[ans] - avg) > abs(a - avg):
        ans = i
print(ans)