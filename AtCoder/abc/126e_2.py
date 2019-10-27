from collections import deque

N , M = map(int,input().split())

checked = [False] * N

edge = [ [] for _ in range(N) ]

for _ in range(M) :
    x , y , z = map(int,input().split())
    edge[x - 1].append(y-1)
    edge[y - 1].append(x-1)

component = 0

for c , check in enumerate(checked) :
    if check :
        continue

    stack = deque([c])
    component += 1

    while stack :
        current = stack.pop()

        if checked[current] :
            continue

        checked[current] = True
        for v in edge[current] :
            if not checked[v] :
                stack.append(v)

print(component)