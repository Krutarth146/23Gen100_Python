# start = 24
# end = 10000
# count = 0
# outer = 0

# num = start   # num = 1   
# while num<=end:  # 24 to 10000    num = 24
#     i = 1
#     sum = 0
#     while i<num:   #  1 to 23
#         if num % i == 0:   # 24 % 1 == 0
#             sum = sum + i   # 1 + 2 + 3 + 4 + 6 + 8 + 12 =  >24
#         i+=1
#         count+=1


#     if sum == num:
#         print(num)

#     num+=1
#     outer += 1

# print(count)   # 49994747  -> Total count of Inner loop
# print(outer)   # 9977      -> Total count of Outer loop


# Armstrong, Plindrome, Prime, Perfect, Twin




# x = None
# print(type(x))   # <class 'NoneType'>

# h = True   # -> 1
# print(type(h))   # Implicit Typeconversion
# g = 90   
# print(type(g))   # 
# print(h+g)   # 91



# # ------------------  FOR LOOP   ------------------------------------

# # for(i=0 ; i<=100 ; i++)
# # {

# # }

# for i in range(10):   # -> starts from 0 default, end (n-1)
#     print(i,end=' ')  # 0 1 2 3 4 5 6 7 8 9

# print()
# for _ in range(1,16):
#     print(_,end=' ')  # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15


# print()
# for _ in range(1,16,1):   # start: end (n-1): step(n-1)
#     print(_,end=' ')  # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

# print()
# for _ in range(1,16,3):   # start: end (n-1): step(n-1)
#     print(_,end=' ')  # 1 4 7 10 13

# print()
# for _ in range(0,101,2):   # start: end (n-1): step(n-1)
#     print(_,end=' ')  # 1 4 7 10 13


# print()
# for _ in range(99,0,-2):   # start: end (n-1): step(n-1)

#     if _ % 5 == 0 or _ % 7 == 0:
#         print(_,end=' ')  # 1 4 7 10 13

list1 = [10, 20, 30, 40]
print(len(list1))   # 4
list2 = [[1,2,3] , [4, 5, 6], [8,9,7]]
print(len(list2))   # 3


print(list2[0])  # [1, 2, 3]

print(list2[0][1])


for k in list2:
    for g in k:
        print(g,end=' ')   # [1, 2, 3]   [4, 5, 6]  [8, 9, 7]


for r in range(3):
    for t in range(0,r-1,-1):
        print(list2[r][t],end=' ')   # 1 2 3 4 5 6 8 9 7 1