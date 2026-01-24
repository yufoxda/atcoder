import math
n,m = map(int, input().split())

# [[]] a as index ,B list
# 利害関係のリスト
A = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    A[a-1].append(b-1)
    A[b-1].append(a-1)
for i in range(n):
    
    if n-len(A[i])-1 < 3:
        print(0,end=" ")
        continue
    
    print(math.comb(n-len(A[i])-1,3),end=" ")
