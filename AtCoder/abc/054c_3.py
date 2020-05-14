from itertools import permutations

N, M = map(int, input().split())

toList = [set() for _ in range(N)]
for _ in range(M):
    fr, to = map(lambda a: int(a) - 1, input().split())
    toList[fr].add(to)
    toList[to].add(fr)

def countPath():
    ret = 0
    for P in permutations(range(N), r=N):
        if P[0] != 0:
            continue
        for fr, to in zip(P, P[1:]):
            if not to in toList[fr]:
                break
        else:
            ret += 1
    return ret

print(countPath())
