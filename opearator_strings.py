# Membership Operators

# in , not in

# list1 = [10,20,90.89,True, [2,3,5], 3+5j, "Harsh"]
# print(list1)  # [10, 20, 90.89, True, [2, 3, 5], (3+5j), 'Harsh']

# fruits = ['apple', 'banana', 'lichi', 'chickoo']

# fruit_input = input("Enter any fruit name: ")   # pineple

# for i in fruits:   # linear Search
#     if i == fruit_input:
#         print(f"{fruit_input} is available")
#         break


# # ---------------------------
# if fruit_input in fruits:
#     print(f"{fruit_input} is available")  # lichi is available
# else:
#     print("Not Available")



# Identity Operator
# is , is not

x = [10,20,30,40,50]
y = [10,20,30,40,50]

# x = 90
# y = 90

print(id(x))  # 1462630602752
print(id(y))  # 1462630757120


if x is y:
    print(True)
else:
    print(False)


z = x

print(id(x))  # 1462630602752
print(id(z))  # 1462630602752

if x is z:
    print(True)  # True
else:
    print(False)


# --------------------------------------------------------------

# String

str1 = 'Marlin'
print(str1)
print(type(str1))  # <class 'str'>

str2 = '90'
print(type(str2))  # <class 'str'>

str3 = "ROyal_is Best Institute Ever123."
       #0123456789...... 
                                    # -1
# Indexing of String

print(str3[0])   # R
print(str3[4])   # l
print(str3[-1])   # .
print(str3[-5])   # r
print(str3[-9])   #   (space)

# Slicing

str3 = "ROyal_is Best Institute Ever123."

# print(str3[start : end(n-1)])

print(str3[0 : 6])  # start - 0, end = 5 -> ROyal_

print(str3[4 : 7])  # Start - 4, end = 6 -> l_i
print(str3[7 : 4])  # blank
print(str3[7 : ])  # s Best Institute Ever123.
print(str3[ : 5])  # starts from 0 , end - 5-1 = 4  # ROyal
print(str3[ : ])  # ROyal_is Best Institute Ever123.
print(str3[-5:-1])  # r123
print(str3[-9:])  #  Ever123.
print(str3[-9:3])  #      (Blank)
print(str3[:-1])  # ROyal_is Best Institute Ever123


# --------------------------

# print(str3[start : end(n-1) : step(n-1)])
str3 = "ROyal_is Best Institute Ever123."

print(str3[0:8:])  # ROyal_is
print(str3[0:8:1])  # ROyal_is  # default 1
print(str3[0:8:3])  # Rai  # default 1
print(str3[2::2])  # yli etIsiueEe13
print(str3[3:1:2])  # (blank)
print(str3[1:2:2])  # O
print(str3[1:1:2])  # (blank)
print(str3[::4])  # Rl tsuE1
print(str3[3:9:2])  # a_s

# -----------

print(str3[4:1:-1])   # lay
print(str3[10:1:-3])   # esl
print(str3[10:0:-3])   # eslO
print(str3[10:-1:-3])   # blank
print(str3[10::-2])   # e ilyR

print(str3[1 :7 :2])  # Oa_
print(str3[5: -2 : -2])  # 
print(str3[5: -2 : 2])  # _sBs nttt vr2

c = 90
f = '90'

print(id(c))  # 2571189554192
print(id(f))  # 2571190844336

if c is f:
    print(True)