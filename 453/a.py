n = int(input())
s = input()
flag = True
for i in s:
    if i == 'o' and flag:
        continue
    else:
        flag = False
        print(i, end='')