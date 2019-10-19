from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

numCnt = defaultdict(int)

for a in A:
    numCnt[a] += 1

for _ in range(M):
    B, C = map(int, input().split())
    numCnt[C] += B

ans = 0
numList = list(numCnt.items())
numList.sort(reverse=True)

for num, cnt in numList:
    while N > 0 and cnt > 0:
        ans += num
        N -= 1
        cnt -= 1

print(ans)