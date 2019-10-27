N, K = map(int, input().split())
D = set(input().split())

ans = N
while True:
    for s in str(ans):
        if s in D:
            break
    else:
        print(ans)
        break
    ans += 1

