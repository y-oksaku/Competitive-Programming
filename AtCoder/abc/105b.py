N = int(input())

def exists():
    for seven in range(N):
        M = N - seven * 7
        if 0 <= M and M % 4 == 0:
            return True
    return False

print('Yes' if exists() else 'No')
