
def haiteru_list(n, w):
    haitteru = []
    for i in range(w):
        tmphaiteru = []
        for j in range(n):
            if ((j+1+i) % (2*w)) < w:
                tmphaiteru.append(j)
        haitteru.append(tmphaiteru)
    return haitteru

t = int(input())
nws = []
cs = []
for _ in range(t):
    n ,w = map(int, input().split())
    c = list(map(int, input().split()))
    nws.append((n, w))
    cs.append(c)



tmp = []
for k in range(t):
    haitteru = haiteru_list(nws[k][0], nws[k][1])
    
    ansarray2 = []
    for i in range(len(haitteru)):
        tmpppp = 0
        for j in haitteru[i]:
            tmpppp += cs[k][j]
        ansarray2.append(tmpppp)

    print(min(ansarray2))
