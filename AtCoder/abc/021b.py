N = int(input())
S, T = map(int, input().split())
K = int(input())
P = list(map(int, input().split())) + [S, T]

print('YES' if len(P) == len(set(P)) else 'NO')
