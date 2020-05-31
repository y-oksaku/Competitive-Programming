N = int(input())
A = list(map(int, input().split()))

if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()

if A[0] != 0:
    print(-1)
    exit()

ans = 1
prev = 1
P = []
for a in A[1:]:
    P.append(prev)
    mx = prev * 2

    if mx < a:
        print(-1)
        exit()

    ans += mx
    prev = mx - a

while prev and P:
    ans -= prev
    pr = P.pop()
    prev = max(0, prev - pr)

print(ans)
