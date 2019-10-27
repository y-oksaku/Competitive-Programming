N = int(input())
M = int(input())

isLeaf = [True] * N
ans = [-1] * N
ans[N - 1] = 1

child = [[] for _ in range(N)]
for _ in range(M):
    pr, cnt, ch = map(int, input().split())
    pr -= 1
    ch -= 1
    child[pr].append((ch, cnt))
    isLeaf[ch] = False

def search(now):
    if ans[now] != -1:
        return ans[now]

    ret = 0
    for ch, cnt in child[now]:
        ret += search(ch) * cnt

    ans[now] = ret
    return ret

for i in range(N):
    search(i)

ans = [a if isLeaf[i] else 0 for i, a in enumerate(ans[:N - 1])]
print(*ans, sep='\n')
