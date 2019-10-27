N, M = map(int, input().split())

cities = [[] for _ in range(N)]

for i in range(M) :
    p, y = map(int, input().split())
    cities[p - 1].append((i, y))

id = [0] * M

for p, city in enumerate(cities) :
    city.sort(key = lambda A : A[1])
    for index, (i, year) in enumerate(city) :
        id[i] = '{pre:06}{i:06}'.format(pre = p + 1, i = index + 1)

for i in range(M) :
    print(id[i])