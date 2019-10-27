N = int(input())
A = list(map(int, input().split()))
B = set([])

for a in A:
    while a % 2 == 0:
        a //= 2
    B.add(a)

print(len(B))