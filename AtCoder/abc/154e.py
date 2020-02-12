N = input()
K = int(input())

def search(d, k, isLess):
    if k == K:
        return 1
    if d == len(N):
        return 0

    ret = search(d + 1, k, isLess or int(N[d]) > 0)

    if k < K:
        if isLess:
            ret += search(d + 1, k + 1, True) * 9
        elif int(N[d]) > 0:
            ret += search(d + 1, k + 1, True) * (int(N[d]) - 1) + search(d + 1, k + 1, False)

    return ret

ans = search(0, 0, False)
print(ans)