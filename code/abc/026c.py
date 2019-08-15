N = int(input())

class node:
    def __init__(self):
        self.child = []


emp = [node() for _ in range(N)]

for i in range(1, N):
    parent = int(input())
    emp[parent - 1].child.append(i)

def calc(num):
    if not emp[num].child:
        return 1

    salalyList = []
    for child in emp[num].child:
        salalyList.append(calc(child))

    return min(salalyList) + max(salalyList) + 1

ans = calc(0)

print(ans)
