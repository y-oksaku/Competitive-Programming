N, K = map(int, input().split())
S = list(input())
T = list(sorted(S))

def diff(A, B) :
    A.sort()
    B.sort()
    pos = 0
    count = 0
    for i in range(len(A)) :
        for j in range(pos, len(B)) :
            if A[i] == B[j] :
                pos = j + 1
                count += 1
                break
            elif A[i] < B[j] :
                pos = j
                break
    return len(A) - count

ans = ''

for i in range(N) :
    for t in T :
        subT = T.copy()
        subT.remove(t)
        if diff(S[i + 1:], subT) + (S[i] != t) <= K :
            if S[i] != t :
                K -= 1
            ans += t
            T = subT
            break

print(ans)
