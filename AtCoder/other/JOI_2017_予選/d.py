import sys
input = sys.stdin.buffer.readline

M = int(input())
A = [tuple(map(int, input().split())) for _ in range(M)]

N = int(input())
B = [tuple(map(int, input().split())) for _ in range(N)]
S = set(B)

def exists(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]

    for ax, ay in A:
        ax += dx
        ay += dy
        if not (ax, ay) in S:
            return False
    return True

for a in A:
    for b in B:
        if exists(a, b):
            print(b[0] - a[0], b[1] - a[1])
            exit()
