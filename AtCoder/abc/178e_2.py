N = int(input())

def rot(x, y):
    return (x - y, x + y)

UV = [rot(*map(int, input().split())) for _ in range(N)]

mxU = max(u for u, _ in UV)
miU = min(u for u, _ in UV)
mxV = max(v for _, v in UV)
miV = min(v for _, v in UV)

print(max(mxU - miU, mxV - miV))
