n , a0 , b0 , c0 , d0 = map(int,input().split())
s = input()

# a < b に変換する
if a0 > b0 : # 入れ替える
    a = b0
    b = a0
    c = d0
    d = c0
else : # 入れ替えない
    a = a0
    b = b0
    c = c0
    d = d0

right = max(c,d)
left = min(a,b)
middle = max(a,b)

for i in range(n-1) :
    if s[i] == '#' and s[i+1] == '#' : # 岩が2個連続である場合
        if i <= right - 2 and i >= left - 1 :
            print('No')
            break
else :
    if c < d :
        print('Yes')
    else :
        for i in range(n-2) :
            if s[i] == '.' and s[i+1] == '.' and s[i+2] == '.' : # 入れ替え可能
                if i + 1 == b - 1 :
                    print('Yes')
                    break
                if i <= d - 2 and i >= b - 1 :
                    print('Yes')
                    break
        else :
            print('No')
