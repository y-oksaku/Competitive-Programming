from collections import defaultdict

N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

def search(sportList):
    if not sportList:
        return float('inf')

    cnt = defaultdict(int)

    for p in range(N):
        for a in A[p]:
            if a in sportList:
                cnt[a] += 1
                break

    maxSport = -1
    ret = -float('inf')
    for s, c in cnt.items():
        if ret < c:
            maxSport = s
            ret = c

    sportList.remove(maxSport)
    return min(cnt[maxSport], search(sportList))

sportList = set(range(1, M + 1))
ans = search(sportList)

print(ans)