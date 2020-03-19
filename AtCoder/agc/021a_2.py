N = input()

def search(digit, isLess):
    if digit >= len(N):
        return 0

    ret = 0
    if isLess:
        ret = max(ret, search(digit + 1, True) + 9)
    else:
        for i in range(int(N[digit])):
            ret = max(ret, search(digit + 1, True) + i)
        ret = max(ret, search(digit + 1, False) + int(N[digit]))
    return ret

ans = search(0, False)
print(ans)
