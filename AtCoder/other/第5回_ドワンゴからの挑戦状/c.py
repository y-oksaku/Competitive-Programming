N = int(input())
S = input()
_ = input()
K = list(map(int, input().split()))

def sol(k):
    ret = 0

    right = 0
    c = 0
    m = 0
    mc = 0
    nx = 0
    for left, s in enumerate(S):
        while right < N and right - left < k:
            if S[right] == 'M':
                nx += 1
            elif S[right] == 'C':
                m += nx
                mc += m
                nx = 0
                c += 1
            right += 1

        if s == 'D':
            ret += mc
        elif s == 'M':
            mc -= c
            m -= 1
        elif s == 'C':
            c -= 1

    return ret

for k in K:
    print(sol(k))
