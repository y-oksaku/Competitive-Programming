S = list(input())

uniq = list(set(S))

if len(uniq) != 2 :
    print('No')
else :
    count = {}
    for s in S :
        if s in count :
            count[s] += 1
        else :
            count[s] = 1

    if count[uniq[0]] == 2 :
        print('Yes')
    else :
        print('No')