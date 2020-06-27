N = int(input())
A = [list(input()) for _ in range(N)]
A = list(zip(*A))

print('\n'.join(''.join(a[::-1]) for a in A))
