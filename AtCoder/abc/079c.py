S = list(map(int, list(input())))

def sol() :
    for i in range(8) :
        s = S[0]
        ret = [-1] * 3
        for j in range(1,4) :
            mask = 2**(j - 1)
            op = i & mask
            if op == 0 :
                s += S[-j]
                ret[-j] = '+'
            else :
                s -= S[-j]
                ret[-j] = '-'
        if s == 7 :
            return ret
    return -1

ans = sol()

print(S[0], end='')
for i in range(3) :
    print(ans[i], end='')
    print(S[i+1], end='')
print('=7')