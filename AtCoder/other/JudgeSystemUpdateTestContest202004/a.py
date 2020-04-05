S, L, R = map(int, input().split())

if L <= S <= R:
    print(S)
elif S < L:
    print(L)
else:
    print(R)
