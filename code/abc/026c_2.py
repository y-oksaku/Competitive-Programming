def sol():
    N = int(input())
    child = [[] for _ in range(N)]

    for i in range(1, N):
        b = int(input())
        b -= 1
        child[b].append(i)

    def seach(now):
        money = []
        for to in child[now]:
            money.append(seach(to))

        ret = 1
        if money:
            ret += max(money) + min(money)

        return ret

    print(seach(0))

sol()
