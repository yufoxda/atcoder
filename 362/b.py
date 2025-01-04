p = []
for i in range(3):
    p.append(list(map(int,input().split())))
a = [p[1][0]-p[0][0],p[1][1]-p[0][1]]
b = [p[2][0]-p[0][0],p[2][1]-p[0][1]]
c = [b[0]-a[0],b[1]-a[1]]
if(a[0]*b[0] + a[1]*b[1] == 0 or a[1]*c[1]+a[0]*c[0]==0 or b[1]*c[1]+b[0]*c[0]==0):
    print("Yes")
else:
    print("No")