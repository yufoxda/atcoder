a,b,xx = map(int, input().split())
cc = 0
d=0
def aaa(xxx):
    c=1
    x=0
    n=0
    while(n<x):
        c*=10
        d = len(str(c))
        n = a*c+b*d
    c/=10
    
    d=len(str(c))
    if(d<=1):
        return(cc)
    x-=a*c+b*c
    aaa(x)
print(aaa(xx))