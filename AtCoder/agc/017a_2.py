N, P = map(int, input().split())
A = list(map(lambda a: int(a) % 2, input().split()))

if P == 1 and A.count(1) == 0:
    print(0)
    exit()

if P == 0 and A.count(1) == 0:
    print(2**N)
    exit()

print(2**(N - 1))