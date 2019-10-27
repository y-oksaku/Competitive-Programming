N , K = map(int,input().split())
S = list(map(int,list(input())))

# ランレングス符号化
# (1 0 1 0 ... 0 1)の数を数える
count = []

if S[0] == 0 :
    count.append(0)

index = 0

while index < N :
    now = S[index]
    end = index + 1  # 異なる値の左端のインデックス
    while end < N :
        if S[end] != now :
            break
        end += 1
    count.append(end - index)
    index = end

if S[-1] == 0 :
    count.append(0)

L = len(count)

sub = sum(count[0 : 2 * K + 1])
ans = sub

i = 2
while (i + 2*K) < L :
    sub = sub - count[i-1] - count[i-2] + count[i+2*K] + count[i+2*K - 1]
    if sub > ans :
        ans = sub
    i += 2

print(ans)