# 24 -> 1,2,3,4,6,8,12,24
# 56 -> 1,2,4,7,8,14,28,56
# 53 -> 1, 53
# 29 -> 1, 29

# num = int(input())   # 24
# divisors = 0

# i=1
# while i<=num:   # i = 3
#     if num % i == 0:  # 24 % 3 == 0
#         print(i,end=' ')   # 1 2 3
#         divisors+=1
#     i+=1 


# print()
# print(divisors)
# if divisors == 2:
#     print("Prime Num")



# 153 -> 3*3*3 + 5*5*5 + 1*1*1

# 8208 -> 8*8*8*8 + 0 + 2*2*2*2 + 8*8*8*8 = 8208


# 835  ->  538
num = int(input())
length = len(str(num))  # Explicit Typecasting


sum = 0
safe = num
while num != 0:  # 528  -> 825
    rem = num % 10   # rem = 
    # sum  += rem ** length   # 5 ** 3   # 125 (opearator asoociativity) 125+ 27 = 152 + 512 = 664
    # if rem % 2 != 0:
    #     sum  = sum + rem  # 5+ 3 + 8 = 16  (sum of odd digits)   # 15
    sum = sum * 10 + rem    # sum =  825
    num = num // 10  # num = 0

print(sum)


if sum == safe:   # 153 == 153
    print("Armstrong")
