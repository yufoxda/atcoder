import math
a = int(input())
n= input()
nn = list(n)

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

def check(num, sin):
    num_str = str(num)
    num_str2 = ''.join(list(reversed(num_str)))
    if num_str == num_str2 :
        s1 = base10int(num,sin)
        sstr2 = ''.join(list(reversed(s1)))
        return s1 == sstr2
    return False

ans = 0

# 151 3/2 = 1.5 => 1 
# 1 1/2 0.5 => 0

# 1115111 の次　
# 1116111

# 5554555
# 5555555
# 5556555
# 5557555

# 5560555
# 5560655


# if(check(i, a)):
#         ans += i
zyouken = math.ceil(len(nn)/2)
print(zyouken)

# 偶数桁パリンドローム (11, 1221, 123321, ...)
i = 1
while True:
    aaa = int(str(i) + str(i)[::-1])
    if aaa > int(n):
        break
    if check(aaa, a):
        ans += aaa
    i += 1

# 奇数桁パリンドローム (121, 12321, 1234321, ...)  
i = 1
while True:
    aaa = int(str(i) + str(i)[-2::-1])
    if aaa > int(n):
        break
    if check(aaa, a):
        ans += aaa
    i += 1
    
print(ans)

    