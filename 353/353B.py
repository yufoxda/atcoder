n,k=map(int,input().split())
a = list(map(int,input().split()))

ans = 0
nowk=0
skip=0
i=0
ii=0

while(i<n):
    nowk=a[i]
    ii=i
    while(i<n-1):
        if(nowk+a[i+1]<=k):
            nowk+=a[i+1]
            i+=1
        else:
            break
    ans+=1
    i+=1

print(ans)