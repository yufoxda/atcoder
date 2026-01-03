s = list(input())

flag = False
for i in range(len(s)):
    if(s[i] == '#'):
        if(flag):
            flag = False
            print(i+1)
        else:
            print(str((i+1))+",", end='')
            flag = True
