S = input()

for s in range(3) :
    if S[s] == S[s+1] :
        print('Bad')
        break
else :
    print('Good')
