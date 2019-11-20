from collections import defaultdict
N = int(input())

SP = defaultdict(list)
for i in range(1, N + 1):
    S, P = input().split()
    SP[S].append((int(P), i))

items = list(SP.items())
items.sort()
for _, A in items:
    A.sort(reverse=True)
    for _, i in A:
        print(i)

