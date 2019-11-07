from bisect import bisect_left
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

matchNum = {
    1 : 2,
    2 : 5,
    3 : 5,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 3,
    8 : 7,
    9 : 6,
}

makeDigit = [-float('inf')] * (N + 1)
makeDigit[0] = 0
for n in range(1, N + 1):
    d = makeDigit[n]
    for k in nums:
        cnt = n - matchNum[k]
        if cnt >= 0:
            d = max(d, makeDigit[cnt] + 1)
    if makeDigit[n] < d:
        makeDigit[n] = d

ans = []
for d in range(makeDigit[N])[:: -1]:
    for k in nums:
        cnt = N - matchNum[k]
        if cnt >= 0 and makeDigit[cnt] == d:
            ans.append(k)
            N = cnt
            break

ans.sort(reverse=True)
print(int(''.join(map(str, ans))))
