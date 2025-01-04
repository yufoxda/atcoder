x = int(input())
n = 0
for i in range(1,10):
    if(x % i == 0):
        if(x / i <= 9):
            n+=1
print(2025 - x * n)
