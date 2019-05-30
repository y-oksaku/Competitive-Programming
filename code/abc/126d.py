import numpy as np
N = int(input())

edge = np.zeros((N,N))
color = [0] * (N)

for i in range(N-1) :
    u , v , w = map(int,input().split())
    edge[u-1,v-1] = w
    edge[v-1,u-1] = w

color[0] = 1
stack = [0]

while len(stack) > 0 :
    v = stack.pop() # 現在の頂点

    for i in range(N) :
        if edge[v][i] > 0 and color[i] == 0 : # 辺があり，色がついていない場合
            if edge[v][i] % 2 == 0 :
                color[i] = color[v]
            else :
                color[i] = color[v] * -1
            stack.append(i)

for i in range(N) :
    if color[i] == 1 :
        print('1')
    else :
        print('0')