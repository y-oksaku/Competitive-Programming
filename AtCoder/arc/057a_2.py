A, K = map(int, input().split())
MX = 2 * 10**12

if K == 0:
    print(MX - A)
    exit()

now = A
for d in range(10**9):
    if now >= MX:
        print(d)
        break
    now += 1 + K * now
