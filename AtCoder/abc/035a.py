W, H = map(int, input().split())

if abs(W / H - 4 / 3) < abs(W / H - 16 / 9):
    print('4:3')
else:
    print('16:9')