N, M = map(int, input().split())

def sol(N):
    if N == 1:
        return []

    N += 1
    ans = [[] for _ in range(N)]

    K = 0
    for i, n in enumerate(range(1, N // 2)):
        ans[i].append(n)
        K += 1
    for i, n in enumerate(range(N // 2, N - 1)):
        ans[K - 1 - i].append(n)

    return ans

if N % 2 == 1:
    ans = sol(N)
    for a in ans[:M]:
        print(*a)
else:
    L = N // 2
    ans = []

    if L % 2 == 0:
        for a in sol(L + 1):
            if len(a) == 0:
                continue
            ans.append(a)
        for a in sol(L - 1):
            if len(a) == 0:
                continue
            a[0] += L + 1
            a[1] += L + 2
            ans.append(a)
        for a in ans[:M]:
            print(*a)
    else:
        for a in sol(L):
            if len(a) == 0:
                continue
            ans.append(a)
        for a in sol(L):
            if len(a) == 0:
                continue
            a[0] += L
            a[1] += L + 1
            ans.append(a)
        for a in ans[:M]:
            print(*a)
