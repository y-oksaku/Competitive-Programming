N, D = map(int,input().split())

X = []

for _ in range(N) :
    X.append(list(map(int,input().split())))

ans = 0

for i in range(N) :
    for j in range(i+1,N) :
        x = X[i]
        y = X[j]
        dist = 0
        for k in range(D) :
            dist += (x[k] - y[k])**2
        b = int(dist**0.5)
        if abs(b**2 - dist) < 1e-10 :
            ans += 1

print(ans)