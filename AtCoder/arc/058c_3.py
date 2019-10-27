N, K = map(int, input().split())
D = set(input().split())

ans = N
while any([i in D for i in str(ans)]):
    ans += 1

print(ans)