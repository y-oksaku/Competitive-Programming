S = input()
N = int(input())
T = []

for s1 in S:
    for s2 in S:
        T.append(s1 + s2)

T.sort()
print(T[N - 1])