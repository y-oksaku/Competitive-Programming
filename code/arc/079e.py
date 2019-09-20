N = int(input())
A = list(map(int, input().split()))

ans = 0

while max(A) >= N:
    maxIndex = A.index(max(A))
    cnt = A[maxIndex] // N
    for i in range(N):
        if i == maxIndex:
            A[i] -= N * cnt
        else:
            A[i] += cnt
    ans += cnt

print(ans)