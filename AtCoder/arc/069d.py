N = int(input())
S = list(input())

# Sの値を+-1にする
for i in range(N) :
    if S[i] == 'o' :
        S[i] = 1
    else :
        S[i] = -1

S.append(S[0])

def check() :
    for first in [1, -1] :
        for second in [1, -1] :
            animal = [1] * (N + 2)
            animal[0] = first
            animal[1] = second
            for i in range(1,N+1) :
                if animal[i] == 1 :  # 動物が羊の場合
                    animal[i+1] = animal[i-1] *  S[i]
                else :  # 動物が狼の場合
                    animal[i+1] = animal[i-1] * S[i] * (-1)
            if animal[-2] == first and animal[-1] == second :
                return animal
    return -1

ans = check()

if ans == -1 :
    print(-1)
else :
    for i in range(N) :
        if ans[i] == 1 :
            print('S', end='')
        else :
            print('W', end='')
    print('')
