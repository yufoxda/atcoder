n = int(input())
t = list(map(int, input().split()))
temp =[]
for i in range(n):
    temp.append([t[i], i+1])
temp.sort()

print(temp[0][1]  , temp[1][1] , temp[2][1])