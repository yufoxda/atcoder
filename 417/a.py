s = input()

i = int(s[0])
j = int(s[-1])

if(j<8):
    j += 1
elif (j==8 and i < 8):
    j = 1
    i += 1

print(str(i) + "-" + str(j))