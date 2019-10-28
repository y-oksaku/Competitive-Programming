N = int(input())
S = input()

V = set()
for s in S:
    if s in V:
        V.remove(s)
    else:
        V.add(s)

print(len(V))