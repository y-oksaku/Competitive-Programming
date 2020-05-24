N, M = map(int, input().split())

for three in range(N + 1):
    m = M - three * 3

    if m % 2 == 1 or m < 0:
        continue

    m //= 2

    four = m - (N - three)
    two = m - 2 * four

    if min(two, three, four) >= 0:
        print(two, three, four)
        exit()

print(-1, -1, -1)
