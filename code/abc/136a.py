A, B, C = map(int, input().split())

C -= (A - B)
if C < 0 :
    print('0')
else :
    print(C)