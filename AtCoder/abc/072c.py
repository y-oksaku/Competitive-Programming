N = int(input())
A = list(map(int, input().split()))

numCount = [0 for _ in range(10**5 + 1)]

for a in A:
    numCount[a] += 1

ans = 0
for i in range(10**5 + 1):
    if ans < sum(numCount[i: i + 3]):
        ans = sum(numCount[i: i + 3])

print(ans)