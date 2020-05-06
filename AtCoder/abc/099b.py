A, B = map(int, input().split())
H = [i * (i + 1) // 2 for i in range(1, 1001)]

for l, r in zip(H, H[1:]):
    if r - l == B - A:
        print(r - B)
        exit()