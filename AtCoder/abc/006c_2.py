N, M = map(int, input().split())

for three in range(N + 1):
    D = M - three * 3

    if D % 2 == 1:
        continue
    D //= 2
    K = N - three

    four = D - K
    two = K - four

    if min(two, three, four) < 0:
        continue

    if two * 2 + three * 3 + four * 4 == M:
        print(two, three, four)
        exit()

print('-1 -1 -1')