N, K = map(int, input().split())
S = input()

depth = []
now = 0
for s in S:
    if s == '(':
        now += 1
    else:
        now -= 1
    depth.append(now)

depth.sort(reverse=True)
ans = sum(depth[:K])
print(ans)