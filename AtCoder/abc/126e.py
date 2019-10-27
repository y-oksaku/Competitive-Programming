from collections import deque

N , M = map(int,input().split())

edge = [[] for _ in range(N)]

for _ in range(M) :
    x , y , z = map(int,input().split())

    edge[x-1].append(y-1)
    edge[y-1].append(x-1)

check = [False] * N

q = deque([0])
count = 1 # 連結成分の数

while True:
    while q :
        current = q.popleft()

        if not check[current] :
            check[current] = True

            for n in edge[current] :
                if not check[n] :
                    q.append(n)

    for v , status in enumerate(check) :
        if(not status) :
            q = deque([v])
            count += 1
            break
    else :
        break

print(count)


