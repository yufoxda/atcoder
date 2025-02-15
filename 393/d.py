n = int(input())
s = input()
tmp = 0
current_index = 0
firstmove = 0
while(tmp < 2):
    if(tmp == 1):
        firstmove += 1
    if(s[current_index] == '1'):
        tmp += 1
        if(tmp == 2):
            firstmove -= 1

    current_index += 1
   
    if(current_index >= n):
        print(0)
        exit()


secondidx = current_index-1
move = 0
for i in range(current_index, n):
    if(s[i] == '1'):
        firstmove += move
        move -= 1
    move += 1

print(firstmove)