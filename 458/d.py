import bisect


x = int(input())
q = int(input())

# N, Q = map(int, input().split())
ans = []
A = []
n = 1
bisect.insort(A, x)
for _ in range(q):
    a,b = map(int,input().split())
    bisect.insort(A, a)
    bisect.insort(A,b)
    n += 2
    ans.append(A[int((n+1)/2)-1])
    
for i in ans:
    print(i)