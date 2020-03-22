from collections import deque
import sys
input = sys.stdin.buffer.readline

N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    fr, to = map(lambda a: int(a) - 1, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

def calcDist(fr):
    minDist = [10**18] * N
    que = deque([(fr, 0)])

    while que:
        now, dist = que.pop()

        if minDist[now] < dist:
            continue
        minDist[now] = dist

        for to in edges[now]:
            if minDist[to] > dist + 1:
                minDist[to] = dist + 1
                que.append((to, dist + 1))

    return minDist

D0 = calcDist(0)
R = max(calcDist(D0.index(max(D0)))) + 1

print('Second' if R % 3 == 2 else 'First')
