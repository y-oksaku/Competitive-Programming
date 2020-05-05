N, M = map(int, input().split())

edges =[set() for _ in range(N + 1)]
one = set()
for _ in range(M):
    fr, to = map(int, input().split())
    edges[fr].add(to)
    edges[to].add(fr)
    if fr == 1:
        one.add(to)
    if to == 1:
        one.add(fr)

for fr in one:
    if N in edges[fr]:
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')
