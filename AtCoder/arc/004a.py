N = int(input())

P = []
for _ in range(N) :
    x, y = map(int, input().split())
    P.append((x,y))

ans = 0
for i in range(N) :
    for j in range(i+1,N) :
        x1, y1 = P[i]
        x2, y2 = P[j]
        dist2 = ((x1 - x2)**2 + (y1 - y2)**2)
        ans = max(ans, dist2)

print(ans**(0.5))