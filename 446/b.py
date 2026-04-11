n,m = map(int, input().split())

isselected = [False] * m
ans = []

for i in range(n):
    l = int(input())
    x = list(map(int, input().split()))
    canselect = False
    for j in x:
        if not isselected[j-1]:
            isselected[j-1] = True
            ans.append(j)
            canselect = True
            break
    if not canselect:
        ans.append(0)
    
for i in ans:
    print(i)

    
        