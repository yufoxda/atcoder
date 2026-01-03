import math

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

# テストケース
a = 8
n = "999999999999"

ans = 0
found_numbers = []

# 0-9の一桁数字
for i in range(10):
    if i <= int(n) and check(i, a):
        ans += i
        found_numbers.append(i)
        print(f"Found 1-digit: {i}")

print(f"After 1-digit: ans = {ans}")

# いくつかの小さなパリンドロームを手動チェック
test_palindromes = [11, 22, 33, 44, 55, 66, 77, 88, 99, 
                   101, 111, 121, 131, 141, 151, 161, 171, 181, 191,
                   1001, 1111, 1221, 1331, 1441, 1551, 1661, 1771, 1881, 1991]

for p in test_palindromes:
    if p <= int(n) and check(p, a):
        print(f"Found palindrome: {p}, base-{a}: {base10int(p, a)}")
