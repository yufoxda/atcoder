n,m = map(int,input().split())

g =  [[0]*n for _ in range(n)]

for _ in range(m):
    x,y = map(int,input().split())
    g[x-1][y-1] = 1

q = int(input())
kuros =[]
ans = []
def tansaku(g,kuros,v):
    visited = [False]*n
    stack = [v-1]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        elif node in kuros:
            return "Yes"

        visited[node] = True
        for i in range(n):
            if g[node][i] == 1 and not visited[i]:
                stack.append(i)
    return "No"

for _ in range(q):
    num,v = map(int,input().split())
    if num == 1:
        # kurokusuru
        kuros.append(v-1)
    else:
        # dadoritukeruka
        ans.append(tansaku(g,kuros,v))

print('\n'.join(map(str,ans)))


        



