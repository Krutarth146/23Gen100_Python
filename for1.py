_ = 40
print(_)

import random

# pip install numpy

num = random.randrange(1,10)
print(num)


# ------------------------

# for(i=1 ; i<=100 ; ++i)
# {

# }

# i++ -> i = i+1
# ++i -> i = i+1

# for i in range(start , end, step):


# for j in range(10):   # 0 to 9
#     print(j)

# for i in range(1, 101):   # start- 1, end=100
#     print(i,end=' ')

    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99

# for k in range(101,1):
#     print(k)   # return Nothing

# for w in range(23,90,1):
#     print(w)  # 23 to 89

# for e in range(101,201,2):
#     print(e)   # odd from 101 to 200

# for h in range(1,101,4):
#     print(h)   # 1 5 9 ....

# # reverse Index
# for d in range(8,2,-1):
#     print(d,end= ' ')  # 8 7 6 5 4 3
# print()
# for d in range(18,2,-3):   # 3-1 = 2
#     print(d,end= ' ')  # 18 15 12 9 6 3

# print()
# for u in range(2,20,-2):
#     print(u,end=' ')   # No error Returns Nothing

# for x in range(-2,-7,-2):
#     print(x,end=' ')  # -2 -4 -6
# print()

# for x in range(-7,-2,3):
#     if x != -7:
#         print(x,end=' ')  # -4


# -------------------------------
# Break and Continue

for i in range(10):   # i=5
    if i==5:   # 5 == 5
        continue
    print(i,end=' ')   # 0 1 2 3 4 6 7 8 9

print()
l = 3   # Intialization
while l < 13:   # Condition
    if l == 6:   # 6==6
        print(l)   # 6
        l+=1
        continue 
    l+=1    # Flow


# Break Statement
print("------------------------")   # i = 11
while i<15:
    if i==13:
        print(i)
        break
    i+=2

# 13

h = 10

for i in range(h):
    for j in range(0,i-1,-1):
        if i==j:
            break
        print(j)
    print("Harsh",i)