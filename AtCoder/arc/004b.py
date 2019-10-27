N = int(input())
D = [int(input()) for _ in range(N)]

D.sort()

maxAns = sum(D)
minAns = max(0, D[-1] - sum(D[:N - 1]))

print(maxAns)
print(minAns)