n,k = map(int,input().split())
s = list(input())

now1= False
time = 0
index = 0
for i in s:
    if(i == '1' and not now1):
        now1 = True
        time += 1
    elif(i == '0' and now1):
        now1 = False
    if(time == k):
        break
    index += 1
while(s[index-1] == '0'):
    s[index-1] = '1'
    tmp = index
    while( tmp+1 < n and s[tmp+1] != '0'):
        s[tmp] = '1'
        tmp += 1
        s[tmp] = '0'
    index -= 1

for i in s:
    print(i,end="")
print()