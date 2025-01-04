x_in = list(input())
en1=["zero","one","two","three","four","five","six","seven","eight","nine"]
en10s=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eightteen","nineteen"]
en10=["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eightty","ninety"]
en100=["","thousand","million","billion"]
ans = []


def to_english_int(x):
    fase = 0
    en100_index = 0
    for i in reversed(range(len(x))):
        if(fase%3==0):
            ans.insert(0,en100[en100_index])
            en100_index+=1
            fase=0
        if(fase==0):
            ans.insert(0,en1[int(x[i])])
            fase+=1
        elif(fase==1):
            if(int(x[i])==1):
                del ans[0]
                ans.insert(0,en10s[int(x[i+1])])
            elif(int(x[i]) != 0):
                ans.insert(0,en10[int(x[i])])
            fase+=1
        elif(fase == 2):
            ans.insert(0,"hundred")
            ans.insert(0,en1[int(x[i])])
            fase+=1

intnum = 0
pointflag=False
for j in x_in:
    intnum += 1
    if(j=="."):
        to_english_int(x_in[0:intnum-1])
        ans.append("point")
        pointflag=True
    elif(pointflag):
        ans.append(en1[int(j)])
if(not pointflag):
    to_english_int(x_in)

is_first =True
for i in ans:
    if(i==""):
        continue
    if(is_first):
        print(i[0].upper()+i[1:],end=" ")
        is_first=False
        continue
    print(i,end=' ')