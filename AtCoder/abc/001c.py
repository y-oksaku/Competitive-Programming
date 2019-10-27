def sol():
    deg, speed = map(float, input().split())

    directList = ['NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
    direct = directList[int((deg / 10 - 11.25)  / 22.5)]

    if deg < 112.5:
        direct = 'N'

    dis = int(((speed / 60) * 10 + 0.5)) / 10

    if dis <= 0.2:
        direct = "C"
        w = 0
    elif dis <= 1.5:
        w = 1
    elif dis <= 3.3:
        w = 2
    elif dis <= 5.4:
        w = 3
    elif dis <= 7.9:
        w = 4
    elif dis <= 10.7:
        w = 5
    elif dis <= 13.8:
        w = 6
    elif dis <= 17.1:
        w = 7
    elif dis <= 20.7:
        w = 8
    elif dis <= 24.4:
        w = 9
    elif dis <= 28.4:
        w = 10
    elif dis <= 32.6:
        w = 11
    else:
        w = 12

    print('{} {}'.format(direct, w))

sol()

