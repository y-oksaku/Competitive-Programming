W , H , x , y = map(int,input().split())

area = W * H / 2.

if 2 * x == W and 2 * y == H :
    var = '1'
else :
    var = '0'

print('{} {}'.format(area,var))