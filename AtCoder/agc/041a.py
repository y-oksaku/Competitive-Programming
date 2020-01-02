N, A, B = map(int, input().split())
D = B - A
if D % 2 == 0:
    print(D // 2)
else:
    print((D - 1) // 2 + min(A - 1, N - B) + 1)