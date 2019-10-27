N , q = map(int,input().split())

# アルファベットの配列の定義
alph = [''] * N
for i in range(N):
    alph[i] = chr(ord('A') + i)

# ポインタを用いてglobal変数として回数を減らす
Q = [q]

# マージソート (軽いものが先頭)
def mergeSort(sort):
    if len(sort) > 1:
        harf = int(len(sort)/2.)
        len_1 = mergeSort(sort[0:harf])
        len_2 = mergeSort(sort[harf:])

        ret = []

        while(len(len_1) > 0 or len(len_2) > 0):
            if(len(len_1) == 0):
                ret.append(len_2.pop(0))
            elif len(len_2) == 0:
                ret.append(len_1.pop(0))
            else:
                Q[0] = Q[0]-1
                if(Q[0] < 0):
                    exit()
                print('? {} {}'.format(len_1[0],len_2[0]),flush=True)
                arg = input()
                if(arg == '<'):
                    ret.append(len_1.pop(0))
                elif (arg == '>'):
                    ret.append(len_2.pop(0))
                else:
                    pass
        return ret
    else:
        return sort


ans = mergeSort(alph)
out = '! '

while(len(ans) > 0):
    out = out + ans.pop(0)

print(out,flush=True)
exit()