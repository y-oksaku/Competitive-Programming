N = int(input())
while True:
    if len(set(str(N))) == 1:
        print(N)
        break
    N += 1