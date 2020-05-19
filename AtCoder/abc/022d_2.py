N = int(input())
A = [complex(*map(int, input().split())) for _ in range(N)]
B = [complex(*map(int, input().split())) for _ in range(N)]

def calc(X):
    C = sum(X)

    ret = 0
    for x in X:
        ret = max(ret, abs(C - x * N))
    return ret

a = calc(A)
b = calc(B)
print(b / a)
