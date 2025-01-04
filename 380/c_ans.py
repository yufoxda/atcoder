N,K = map(int,input().split())
S = input()

l = [0]
for i in range(1,N):
    if S[i-1]!=S[i]:
        l.append(i)
l.append(N)
idx = l

print(l)

splited_S = [S[idx[i]:idx[i+1]] for i in range(len(idx)-1)]

print(splited_S)