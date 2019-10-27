D = int(input())
N = input()
listN = list(map(int, N))
MOD = 10**9 + 7

allDP = [[0 for _ in range(D)] for _ in range(len(listN) + 1)]  # allDP[digit][sum]
lessNDP = [[0 for _ in range(D)] for _ in range(len(listN) + 1)]  # lessNDP[digit][sum]

allDP[0][0] = 1
lessNDP[0][0] = 1

for digit in range(1, len(listN) + 1) :
    for d in range(D) :
        for i in range(10) :
            allDP[digit][d] = (allDP[digit][d] + allDP[digit - 1][(d - i) % D]) % MOD
            if listN[-digit] == i :  # digit番目がちょうどであるからdigit-1桁目がN以下
                lessNDP[digit][d] = (lessNDP[digit][d] + lessNDP[digit - 1][(d - i) % D]) % MOD
            elif listN[-digit] > i :  # digit番目がNより少ないのでdigit-1桁以下はすべて動く
                lessNDP[digit][d] = (lessNDP[digit][d] + allDP[digit - 1][(d - i) % D]) % MOD

ans = (lessNDP[len(listN)][0] - 1) % MOD
print(ans)