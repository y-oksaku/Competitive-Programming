point = []

for i in range(5) :
    point.append(int(input()))

k = int(input())

for i in range(5) :
    for j in range(5) :
        if abs(point[i] - point[j]) > k :
            print(':(')
            break
    else :
        continue
    break
else :
    print('Yay!')