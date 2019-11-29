H, W = map(int, input().split())
A = [input() for _ in range(H)]

skipRow = set()
skipCol = set()

for h, line in enumerate(A):
    if '#' not in set(line):
        skipRow.add(h)
for w in range(W):
    if all(A[h][w] == '.' for h in range(H)):
        skipCol.add(w)

for i in range(H):
    if i in skipRow:
        continue
    line = [a for w, a in enumerate(A[i]) if w not in skipCol]
    print(''.join(line))