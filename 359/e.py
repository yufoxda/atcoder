n = int(input())
h = list(map(int,input().split()))
j = [0]*len(h)

fullnaw =1
for i in h:
    fullnaw +=i
    print(fullnaw,end=" ")