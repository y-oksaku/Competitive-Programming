N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 任意のiに対して ai <= bi にできればよい

lessA = 0
lessB = 0

for a, b in zip(A, B):
    if a > b:
        lessB += a - b
    elif a < b:
        lessA += (b - a) // 2

if lessB <= lessA:
    print('Yes')
else:
    print('No')

