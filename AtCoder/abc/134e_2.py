from bisect import bisect_right

N = int(input())
S = [1]

for _ in range(N):
    a = int(input())
    a *= -1
    i = bisect_right(S, a)

    if i == len(S):
        S.append(a)
    else:
        S[i] = a

print(len(S))