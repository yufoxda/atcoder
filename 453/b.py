t,x = map(int, input().split())
a = list(map(int, input().split()))

tmp = 0
for i,n in enumerate(a):
    if i==0:
        tmp = n
        print(i, tmp)
        continue
    if(abs(n - tmp) >= x):
        tmp = n
        print(i, n)
    
