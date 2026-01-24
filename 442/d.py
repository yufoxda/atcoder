n,q = map(int, input().split())
a = list(map(int, input().split()))
ans = []
tmp = [0] * (n + 1)
for i in range(n):
    tmp[i + 1] = tmp[i] + a[i]
for i in range(q):
    ttmp = list(map(int, input().split()))
    if len(ttmp) == 2:
        # kueri1
        x = ttmp[1]-1
        sa = a[x+1]-a[x]
        tmp[x+1] = tmp[x+1] + sa
        
        aswap = a[x]
        a[x] = a[x+1]
        a[x+1] = aswap


    else:
        # kueri2
        l,r= ttmp[1], ttmp[2]
        ans.append(tmp[r]-tmp[l-1])

print('\n'.join(map(str, ans)))
