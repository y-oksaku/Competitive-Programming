from collections import defaultdict

N = int(input())

numList = defaultdict(int)

for _ in range(N):
    num = int(input())

    if numList[num] == 0:
        numList[num] = 1
    else:
        numList[num] = 0

ans = sum([c for _, c in numList.items()])
print(ans)