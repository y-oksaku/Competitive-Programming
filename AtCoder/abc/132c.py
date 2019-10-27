N = int(input())
d = list(map(int,input().split()))


d.sort()

right = d[N // 2]
left = d[N // 2 - 1]

if left == right :
    print(0)
else :
    print(right - left)