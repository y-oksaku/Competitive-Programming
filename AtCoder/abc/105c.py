N = int(input())

ans = ''
isOdd = False
while N != 0 :
    if N % 2 == 1 :
        ans += '1'
    else :
        ans += '0'
    if isOdd :
        N += 1
    N //= 2
    isOdd = not isOdd

if ans == '' :
    print('0')
else :
    print(ans[::-1])