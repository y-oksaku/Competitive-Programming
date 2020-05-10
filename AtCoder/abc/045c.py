S = input()
N = len(S)

ans = 0
for d in range(1 << (N - 1)):
    ret = 0
    T = S[0]
    for i, s in enumerate(S[1:]):
        if (d & (1 << i)) > 0 and len(T) > 0:
            ret += int(T)
            T = ''
        T += s
    if len(T) > 0:
        ret += int(T)
    ans += ret
print(ans)
