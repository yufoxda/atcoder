h , w = map(int ,input().split())

s=['.']*(w+2)
first_cant_lake = False
ok_befor = False
cant_time = 0
tmp = [0]*(w+2)

def checks(lists):
    listt = []
    for k in range(len(lists)):
        i=lists[k][0]
        j=lists[k][1]

        if(s[max(i-1,0)][j]  == '#'):
            listt.append([max(i-1,0),j])
        if(s[i][max(j-1,0)]  == '#'):
            listt.append([i,max(j-1,0)])
        if(s[i][min(j+1,w-1)]  == '#'):
            listt.append([i,min(j+1,w-1)])
            
        if(s[min(i+1,h-1)][max(j-1,0)]  == '#'):
            listt.append([min(i+1,h-1),[max(j-1,0)]])
        if(s[min(i+1,h-1)][j]  == '#'):
            listt.append([min(i+1,h-1),j])
        if(s[min(i+1,h-1)][min(j+1,w-1)]  == '#'):
            listt.append([min(j+1,w-1)])
        checks(listt)
    return

    


def check(i,j,updown):
    #上下にあるかどうか
    if(updown):
        if(i-1<0):
            return s[i+1][j] == '#'
        elif(i+1>h-1):
            return s[i-1][j] == '#'
        else:
            return s[i+1][j] == '#' or s[i-1] == '#'
    #左右にあるか
    else:
        if(j-1<0):
            return s[i][j+1] == '#'
        elif(j+1>w-1):
            return s[i][j-1] == '#'
        else:
            return s[i][j+1] == '#' or s[j-1] == '#'


for i in range(h):
    s.append(list(input()))

for i in range(1,h,1):
    for j in range(1,w,1):
        if(s[i,j]=='#'):




print(s)
