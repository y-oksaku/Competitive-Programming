N = int(input())

tNow = 1
aNow = 1

for i in range(N) :
    t, a = map(int, input().split())

    n = max(-(-tNow // t), -(-aNow // a))

    tNow = n * t
    aNow = n * a

print(tNow + aNow)