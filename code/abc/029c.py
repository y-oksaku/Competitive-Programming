N = int(input())

def make(leng, password):
    if leng == N:
        print(password)
        return

    make(leng + 1, password + 'a')
    make(leng + 1, password + 'b')
    make(leng + 1, password + 'c')

make(0, '')