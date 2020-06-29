S = input()
K = int(input())
print(len(set([S[l:l + K] for l in range(len(S) - (K - 1))])) if len(S) >= K else 0)
