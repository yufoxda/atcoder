n, m = map(int, input().split())
graph = [[] for _ in range(n)]
ans = 0
for _ in range(m):
    a, b = map(int, input().split())
    if a == b:
        ans += 1
    elif a < b:
        if(b-1 in graph[a-1]):
            ans += 1
        else:
            graph[a-1].append(b-1)
    else:
        if(a-1 in graph[b-1]):
            ans += 1
        else:
            graph[b-1].append(a-1)
print(ans)  # [[2, 3, 5], ..., [1, 3, 4]]