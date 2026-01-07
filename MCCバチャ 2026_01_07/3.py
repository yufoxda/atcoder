n = int(input())
a = list(map(int, input().split()))

stack = []
sum = 0
for i in a:
    if(stack and stack[-1][0] == i):
        if(stack[-1][1] + 1 >= i ):
            tmp = stack.pop()
            sum -= tmp[1]
        else:
            stack[-1][1] += 1
            sum += 1
    else:
        stack.append([i, 1])
        sum += 1
   
    print(sum)