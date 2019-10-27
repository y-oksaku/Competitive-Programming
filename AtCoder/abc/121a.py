H , W = map(int,input().split())
h , w = map(int,input().split())

white = H * W - h * W - H * w + h * w

print(white)