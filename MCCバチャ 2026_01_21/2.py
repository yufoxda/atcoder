n= int(input())

a = list(map(int,input().split()))

stack = []
ans = 0
for i in range(n):
    if(not stack or stack[-1][0]!=a[i]):
        stack.append([a[i],1])
        ans+=1
    else:
        stack[-1][1]+=1
        ans+=1    
    if(stack[-1][1]>=4):
        aa = stack.pop()
        ans-=4
print(ans)