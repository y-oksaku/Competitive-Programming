N, M = map(int, input().split())

Disk = []
for _ in range(M):
    Disk.append(int(input()))

diskToCase = list(range(N + 1))

prevDisk = 0
for d in Disk:
    diskToCase[prevDisk] = diskToCase[d]
    diskToCase[d] = 0
    prevDisk = d

caseToDisk = {d : i for i, d in enumerate(diskToCase)}

ans = []
for i in range(1, N + 1):
    ans.append(caseToDisk[i])

print(*ans, sep='\n')