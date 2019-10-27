S = input()
K = int(input())

subList = set([])

for front in range(0, len(S)):
    for length in range(1, K + 1):
        subList.add(S[front: front + length])

subList = list(subList)
subList.sort()

print(subList[K - 1])
