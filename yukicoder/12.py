N = int(input())
A = set(map(int, input().split()))

if A == set([2]):
    print(1)
    exit()

def primeList():
    isPrime = [True] * 5000001
    now = 0
    primeRange = [0] * 5000001
    primes = []
    for i in range(2, 5000001):
        if isPrime[i]:
            primes.append(i)
            now += 1
            k = i
            while k <= 5000000:
                isPrime[k] = False
                k += i
        primeRange[i] = now

    return list(primes), primeRange

primes, iToRange = primeList()
gapIndex = []
for i in range(5000000):
    if iToRange[i] != iToRange[i + 1]:
        gapIndex.append(i)

M = len(primes)
ans = 0
left = 0
while left < M:
    V = set()
    right = 0
    for i in range(left, M):
        nums = set(map(int, str(primes[i])))

        if nums.issubset(V):
            continue

        newV = V.union(nums)
        if len(newV & A) == len(newV):
            V = newV
        else:
            right = i
            break
    else:
        if V == A:
            ans = max(ans, 5000000 - left - 1)
            break

    if V == A:
        ans = max(ans, gapIndex[right] - gapIndex[left - 1] - 2)
    left = max(right + 1, left + 1)

if ans == 0:
    print(-1)
else:
    print(ans)