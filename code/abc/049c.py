S = input()
S = S[::-1]

last = ['maerd', 'remaerd', 'esare', 'resare']
length = [5, 7, 5, 6]

index = 0
while index < len(S):
    for i, tail in enumerate(last) :
        sub = S[index:index + length[i]]
        if sub == tail :
            index += length[i]
            break
    else :
        print('NO')
        break
else :
    print('YES')