a,b=map(int,input().split())

tmp = a+b

if((tmp/2).is_integer()):
    print(int(tmp/2))
else:
    print("IMPOSSIBLE")