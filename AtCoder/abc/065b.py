N = int(input())
A = [int(input()) - 1 for _ in range(N)]

now = 0
for i in range(1, N + 1):
    now = A[now]
    if now == 1:
        print(i)
        exit()

print(-1)
