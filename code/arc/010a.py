N, M, A, B = map(int, input().split())
C = [int(input()) for _ in range(M)]

now = N
for i, c in enumerate(C):
    if now <= A:
        now += B
    if now < c:
        print(i + 1)
        break
    now -= c
else:
    print('complete')

