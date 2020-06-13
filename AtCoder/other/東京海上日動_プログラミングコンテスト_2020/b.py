A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

S = V - W
print('NO' if S <= 0 or abs(A - B) > T * S else 'YES')