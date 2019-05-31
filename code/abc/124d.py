N , K = map(int,input().split())
S = input()

length = []
count = 1

# ランレングス符号化
for i in range(N-1) :
    if S[i] == S[i+1] :
        count += 1
    else :
        length.append(count)
        count = 1
else :
    length.append(count)

ans = 0

# iを中心に半径Kの和
for i in range(len(length)) :
    s = sum(length[i-K:i+K+1])
    ans = max(s,ans)

print(ans)