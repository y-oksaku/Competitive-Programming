N = int(input())
A = [(i + 1, a) for i, a in enumerate(map(int, input().split()))]
A.sort(key=lambda A : A[1], reverse=True)

for i, _ in A:
    print(i)
