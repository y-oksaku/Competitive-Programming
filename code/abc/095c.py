A, B, C, X, Y = map(int, input().split())

AandB = X * A + Y * B
allAB = max(X, Y) * 2 * C  # すべてAB

comb = min(X, Y) * 2 * C  # 余らないAB
minXY = min(X, Y)
X -= minXY
Y -= minXY
comb += X * A
comb += Y * B

print(min(AandB, allAB, comb))