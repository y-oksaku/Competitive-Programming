from collections import Counter

N = int(input())
R = input()

cnt = Counter(R)
ansMax = 0
ansMin = float('inf')
for i in range(1, 5):
    ansMax = max(ansMax, cnt[str(i)])
    ansMin = min(ansMin, cnt[str(i)])

print(ansMax, ansMin)