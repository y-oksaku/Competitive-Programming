from string import ascii_lowercase as alph
N = int(input())
A = list(alph)

ans = []

def sol(n):
    global ans

    q, r = divmod(n, 26)
    ans.append(A[r])
    if q > 0:
        sol(q - 1)

sol(N - 1)
print(''.join(ans[::-1]))
