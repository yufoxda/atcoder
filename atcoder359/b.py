n  = int(input())
a = list(map(int,input().split()))
ans =0
for i in range(0,len(a)-2):
    if(a[i]==a[i+2]):
        ans+=1
print(ans)
