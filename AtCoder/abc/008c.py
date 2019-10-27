from itertools import permutations

def sol():
    N = int(input())
    coins = [int(input()) for _ in range(N)]

    ans = 0.0
    for c in coins:
        divCount = -1
        for div in coins:
            if c % div == 0:
                divCount += 1

        if divCount == 0:
            ans += 1
        elif divCount % 2 == 0:
            ans += (divCount + 2) / (2 * divCount + 2)
        else:
            ans += 0.5

    print(ans)

sol()