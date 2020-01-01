X = int(input())

isPrime = [True] * 1000000
for p in range(2, 1000000):
    if not isPrime[p]:
        continue
    if p >= X:
        print(p)
        break
    for i in range(p + p, 1000000, p):
        isPrime[i] = False
