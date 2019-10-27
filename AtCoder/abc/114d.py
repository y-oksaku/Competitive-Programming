N = int(input())

if N <= 9 :
    print(0)
else :
    primeCount = [0] * (N + 1)
    for i in range(2, N + 1) :
        current = i
        for j in range(2, i + 1) :
            while current % j == 0:
                primeCount[j] += 1
                current = current // j

    def primeNum(m) :
        return len(list(filter(lambda x : x >= m - 1, primeCount)))

    ans = 0
    ans += primeNum(75)
    ans += primeNum(25) * (primeNum(3) - 1)  # 3 には 25が含まれる
    ans += primeNum(15) * (primeNum(5) - 1)
    ans += primeNum(5) * (primeNum(5) - 1) * (primeNum(3) - 2) // 2
    print(ans)