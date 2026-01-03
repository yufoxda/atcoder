s = list(input())
flag = False
flag2 = False
for i in range(len(s)):
    if(not flag):
        if(s[i] == '.'):
            flag = True
            print('o', end='')
        else:
            print(s[i], end='')
    else:
        if not flag2:
            if(s[i] == '#'):
                print('#', end='')
                flag2 = True
            else:
                print('.', end='')
        else:
            if(s[i] == '.'):
                print('o', end='')
                flag2 = False
            else:
                print('#', end='')



print()

"""
最初丸
で
＃が来るまで.
#
maru

"""
