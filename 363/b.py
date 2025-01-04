n,t,p = map(int,input().split())
l = list(map(int,input().split()))

l.sort(reverse=True)
if(t-l[p-1] > 0):
    print(t-l[p-1])
    exit()
print(0)
