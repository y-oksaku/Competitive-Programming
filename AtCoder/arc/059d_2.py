S = input()
N = len(S)

def sol():
    for i in range(N - 1):
        T = list(S[i: i + 2])
        if len(set(T)) == 1:
            return (i + 1, i + 2)
    for i in range(N - 2):
        T = list(S[i: i + 3])
        if len(set(T)) <= 2:
            return (i + 1, i + 3)
    return (-1, -1)

print(*sol())
