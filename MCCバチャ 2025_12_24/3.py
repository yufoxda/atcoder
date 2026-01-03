n = int(input())
a = list(map(int, input().split()))

tmp = 0
x = 0
for i in range(n):
    tmp += abs(x - a[i])
    x = a[i]
tmp += abs(x)

for i in range(n):
    if i == 0:
        print(tmp-abs(a[0])-abs(a[0]-a[1])+abs(a[1]))
    elif i == n-1:
        print(tmp-abs(a[n-2]-a[n-1])-abs(a[n-1])+abs(a[n-2]))
    else:
        print(tmp - abs(a[i]-a[i-1]) - abs(a[i+1]-a[i]) + abs(a[i+1]-a[i-1]))
