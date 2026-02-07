n = int(input())
a = list(map(int, input().split())) 
a.sort()
flag = True
ans = []
print(a)
second = [i for i in a if i != max(a)]
print(second)
if second:
    tmp2 = second[0] + second[-1]
    for i in range(1, len(second)//2):
        if second[i] + second[-i-1] != tmp2:
            flag = False
            
            break
    print("test")      
    if flag:
        ans.append(tmp2)
else:
    ans.append(a[0])

print("test")

tmp = a[0] + a[-1]
for i in range(0, n//2):
    if a[i] + a[-i-1] != tmp:
        flag = False
        print(a[i], a[-i-1])
        break
print("test")
if flag:
    ans.append(tmp)



print(*ans)