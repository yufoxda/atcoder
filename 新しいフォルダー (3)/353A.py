a = int(input())
b =  list(map(int,input().split()))
c = b[0]
flag = False

for i in range(1,a):
    if(c<b[i]):
        print(i+1)
        flag = True
        break
if( not flag):
    print(-1)