N, K = map(int, input().split())
A = list(map(int, input().split()))

# 最もきつい検索条件を設定する
# 先頭からの最長共通部分列

search = []
for _ in range(N):
    s = input()
    search.append(s)

result = []
for a in A:
    result.append(search[a - 1])

result.sort()
query = result[0]
M = len(query)

dp = [[] for _ in range(M + 1)]
dp[0] = search[::]

for i, q in enumerate(query):
    for s in dp[i]:
        if len(s) <= i:
            continue
        if s[i] == q:
            dp[i + 1].append(s)

ans = ''
for i, res in enumerate(dp):
    if len(res) == K:
        res.sort()
        if res == result:
            print(ans)
            exit()
        break
    elif i < M:
        ans += query[i]

print('-1')