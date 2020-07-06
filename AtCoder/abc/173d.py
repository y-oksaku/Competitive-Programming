N = int(input())
A = list(map(int, input().split()))
A = A + A
A.sort()

ans = A.pop()
A.pop()
for _ in range(N - 2):
    ans += A.pop()

print(ans)
