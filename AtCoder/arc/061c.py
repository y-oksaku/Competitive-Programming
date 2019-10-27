S = input()

ans = 0
lenS = len(S)
divider = lenS - 1  # +を入れることのできる個数

for i in range(1, lenS + 1) :
    now = int(S[-i])
    mask = 0
    for j in range(i) :
        mask *= 10
        mask += now * 2**(max(0,j-1))

    ans += mask * 2**(divider - i + 1)

print(ans)