n,k = map(int,input().split())
l = []
for i in range(n):
    tmp = list(map(int,input().split()))
    li = tmp[0]
    a = tmp[1:]

    l.append((li,a))
c = list(map(int,input().split()))

b = []
ttmp = 0
anslindex = 0
ansindex = 0
# n:num
# i:index
flag = False
for i,n in enumerate(c):
    anslindex = i
    if(ttmp+(l[i][0] * n) < k):
        ttmp += l[i][0] * n
        continue
    else:
        nokori = k - ttmp
        ansindex = nokori % l[i][0] #amari  = index
        break
print(l[anslindex][1][ansindex-1])