n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

suma= [0]*(n + 1)
sumb= [0]*(n + 1)
sumc= [0]*(n + 1)

for i in range(n):
    suma[i+1]=suma[i]+a[i]
    sumb[i+1]=sumb[i]+b[i]
    sumc[i+1]=sumc[i]+c[i]

maxcount = 0
if n == 3:
    print(a[0] + b[1] + c[2])
    exit()

for i in range(1, n-1):
    for j in range(i + 1, n):
        tmp = suma[i]+(sumb[j]-sumb[i])+(sumc[n]-sumc[j])
        if tmp > maxcount:
            maxcount = tmp
print(maxcount)