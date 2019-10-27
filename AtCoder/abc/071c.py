from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
lengCount = defaultdict(int)
for a in A:
    lengCount[a] += 1

lengList = [[leng, count] for leng, count in lengCount.items()]
lengList.sort(key=lambda A : A[0], reverse=True)

firstLeng = 0
for i in range(len(lengList)):
    if lengList[i][1] >= 2:
        firstLeng = lengList[i][0]
        lengList[i][1] -= 2
        break

secondLeng = 0
for i in range(len(lengList)):
    if lengList[i][1] >= 2:
        secondLeng = lengList[i][0]
        break
print(firstLeng * secondLeng)