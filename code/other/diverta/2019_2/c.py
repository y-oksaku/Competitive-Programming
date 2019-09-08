N = int(input())
A = list(map(int, input().split()))

positive = 0
negative = 0

for a in A:
    if a > 0:
        positive += a
    else:
        negative += a

if positive == 0:  # 全部負
    # 一番大きい数から残りをすべて引く
    A.sort(reverse=True)
    now = A[0]
    ans = []
    for a in A[1:]:
        ans.append((now, a))
        now -= a
    print(now)
    for a in ans:
        print(*a)
elif negative == 0:  # 全部非負
    # 一番小さい数から引いて，最後に大きい数から引く
    A.sort()
    now = A[0]
    ans = []
    for a in A[1: N - 1]:
        ans.append((now, a))
        now -= a
    ans.append((A[-1], now))
    now = A[-1] - now
    print(now)
    for a in ans:
        print(*a)
else:
    A.sort()
    neg = A[0]
    pos = A[-1]
    ans = []
    for a in A[1: N - 1]:
        if a > 0:
            ans.append((neg, a))
            neg -= a
        else:
            ans.append((pos, a))
            pos -= a
    ans.append((pos, neg))
    print(pos - neg)
    for a in ans:
        print(*a)
