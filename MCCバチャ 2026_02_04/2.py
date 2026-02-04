n = int(input())

names = []
flag = 0
flag2 = 0
for _ in range(n):
    s,t = input().split()
    for i in range(len(names)) :
        if names[i][0] == s:
            names[i][0] = None
            flag = 1
        if names[i][1] == t:
            names[i][1] = None
            flag2 = 1
        if names[i][0] == t:
            names[i][0] = None
            flag2 = 1
        if names[i][1] == s:
            names[i][1] = None
            flag = 1
    if flag == 1 and flag2 == 0:
        names.append([None,t])
    elif flag2 == 1 and flag == 0:
        names.append([s,None])
    elif flag == 1 and flag2 == 1:
        names.append([None,None])
    else:
        names.append([s,t])
    flag = 0
    flag2 = 0
    
for i in range(len(names)):
    if names[i][0] == None and names[i][1] == None:
        print("No")
        exit()
print("Yes")