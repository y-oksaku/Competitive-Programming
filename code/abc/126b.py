S = input()

A = int(S[:2])
B = int(S[2:])

def isMonth(i) :
    if i >= 1 and i <= 12 :
        return True
    else :
        return False

if isMonth(A) and isMonth(B) :
    print('AMBIGUOUS')
elif not isMonth(A) and isMonth(B) :
    print('YYMM')
elif isMonth(A) and not isMonth(B) :
    print('MMYY')
else :
    print('NA')