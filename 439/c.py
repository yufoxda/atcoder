n = int(input())


ans =[]
def xkouho(n):
    returnlist = []
    for i in range(1,int(n **0.5)+1):
        returnlist.append(i)
    return returnlist

def ykouho(ykouhos,n):
    returnlist = []
    for i in ykouhos:
        kouho = (n - i**2)**0.5
        if(kouho.is_integer() and i<kouho):
            returnlist.append([i,kouho])
    return returnlist

kouho_list = []
for j in range(1,n +1):
    xkouho_list = xkouho(j)
    tmp =ykouho(xkouho_list,j)
    if tmp:  
        kouho_list.append(tmp)
        ans.append(j)

if kouho_list:
    print(len(kouho_list))
    for i in ans:
        print(i,end=' ')
else:
    print(0)
    print()
            
