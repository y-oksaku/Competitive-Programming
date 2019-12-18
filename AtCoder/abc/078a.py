A, B = input().split()
if A == B:
    print('=')
else:
    print('<>'[A>B::2])