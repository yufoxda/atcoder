n = int (input())
l = []
for i in range(n):
    tmp = list(map(int,input().split()))
    l.append(tmp[1:])

x,y = map(int,input().split())
print(l[x-1][y-1])