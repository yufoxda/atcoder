n = int(input())
lr =[]
for i in range(n):
    lr.append(list(map(int,input().split())))
tmp=[lr[0]]
for i in range(n-1):
    tmp.append([tmp[-1][0] + lr[i][0],tmp[-1][1] + lr[i][1]])

if(tmp[-1][0]<=-lr[-1][0]<=tmp[-1][1] or tmp[-1][0] <= -lr[-1][1] <= tmp[-1][1]):
    print("Yes")
    #ans = [min(max(tmp[-1][0],lr[-1][0]),min(tmp[-1][1],lr[-1][1]))]
    ans =[-1]
    tmp.append([tmp[-1][0] + lr[i][0],tmp[-1][1] + lr[i][1]])
    for i in reversed(range(1,n-1)):
        ans.insert(0,min(max(tmp[i][0],-ans[0]-lr[i][1]),min(tmp[i][1],-ans[0]-lr[i][0])))
    ans.insert(0,-sum(ans))
    print(*ans)


else:
    print("No")