import heapq


x = int(input())
q = int(input())

# N, Q = map(int, input().split())
ans = [x]
tii = []
ooki = []
A = [x]
n = 1

for _ in range(q):
    a,b = map(int,input().split())
    if(a<ans[-1] and b< ans[-1]):
        if(a < b):
            heapq.heappush(tii,a)
            heapq.heappush(ooki,ans[-1])
            ans.append(b)
        else:
            heapq.heappush(tii,b)
            heapq.heappush(ooki,ans[-1])
            ans.append(a)
    elif(a<=ans[-1]<=b):
        heapq.heappush(tii,a)
        heapq.heappush(ooki,b)
        ans.append(ans[-1])
    elif(b<=ans[-1]<=a):
        heapq.heappush(tii,b)
        heapq.heappush(ooki,a)
        ans.append(ans[-1])
    else:
        # ans < a < b
        if(a < b):
            heapq.heappush(tii,ans[-1])
            heapq.heappush(ooki,b)
            ans.append(a)
        else:
            #ans < b < a
            heapq.heappush(tii,ans[-1])
            heapq.heappush(ooki,a)
            ans.append(b)
    
for i in ans[1:]:
    print(i)