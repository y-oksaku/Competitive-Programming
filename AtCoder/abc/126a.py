N , K = map(int,input().split())
S = input()

ans = S[:K-1] + S[K-1].replace('A','a').replace('B','b').replace('C','c') + S[K:]

print(ans)