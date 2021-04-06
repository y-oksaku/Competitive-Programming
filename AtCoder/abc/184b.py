_, X = map(int, input().split())

for s in input():
    X += 1 if s == 'o' else -1
    X = max(0, X)

print(X)
