n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

firstbigger = 1

count = a[0]
for i in range(1,n):
    if(a[i] <= b[i]):
        firstbigger = i
        count += b[i]
        break
    else:
        count += a[i]


secondbigger = firstbigger + 1
for i in range(firstbigger+1,n):
    if(b[i] <= c[i]):
        secondbigger = i
        count += c[i]
        break
    else:
        count += b[i]

for i in range(secondbigger+1,n):
    count += c[i]
    
print(count)