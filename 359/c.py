sx,sy =map(int,input().split())
tx,ty = map(int,input().split())
if((sy%2==0 and sx%2!=0) or (sy%2!=0 and sx%2==0)):
    sx-=1
if(ty%2==0 and tx%2!=0) or (ty%2!=0 and tx%2==0):
    tx-=1

ans=abs(sy-ty)
if(tx-sx >0):

    if(abs(tx-sx)>ans):
        ans += (abs(tx-sx)-ans)//2
elif(tx-sx<0):

    if(abs(tx-sx)>ans):
        ans += (abs(tx-sx)-ans)//2

print(ans)