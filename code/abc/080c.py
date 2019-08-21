N = int(input())
F = [[0 for _ in range(10)] for _ in range(N)]
P = [[0 for _ in range(10)] for _ in range(N)]

for i in range(N) :
    F[i] = list(map(int, input().split()))
for i in range(N) :
    P[i] = list(map(int, input().split()))

ans = -float('inf')
for mask in range(1, 2**10) :
    profit = 0
    for shop in range(N) :
        count = 0
        for time in range(10) :
            if (mask & (1 << time) != 0) and F[shop][time] == 1 :
                count += 1
        profit += P[shop][count]
    ans = max(ans, profit)

print(ans)