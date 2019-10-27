N = int(input())
A = [int(input()) for _ in range(N)]

if A[0] > 0:
    print(-1)
    exit()

ans = 0
prev = 0

for a in reversed(A):
    if prev > 0:
        if a == (prev - 1):
            prev = a
            continue
        elif a < prev:
            print(-1)
            exit()
    ans += a
    prev = a

print(ans)
