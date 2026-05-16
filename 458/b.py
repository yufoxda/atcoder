h, w = map(int,input().split())

if(h == 1 and w == 1):
    print("0")
    exit()
if(h == 1):
    print("1",end ="")
    for i in range(1,w-1):
        print(" 2",end="")
    print(" 1")
    exit()
if(w == 1):
    print("1")
    for i in range(1,h-1):
        print("2")
    print("1")
    exit()
for i in range(h):
    for j in range(w):
        if(i == 0 or i == h-1):
            if(0 <j < w-1 ):
                print(" 3",end="")
            else:
                print(" 2",end="")
        else:
            if(0 <j < w-1 ):
                print(" 4",end="")
            else:
                print(" 3",end="")
    print("")

