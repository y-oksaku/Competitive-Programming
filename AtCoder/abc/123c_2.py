N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def ceil(a,b) :
    return (a + b - 1) // b

time =[A , B , C , D , E]
time.sort()

minTime = time[0]

ans = ceil(N,minTime) + 4

print(ans)
