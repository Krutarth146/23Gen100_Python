# Matrix

list1 = [[10,20,30], 
         [40,50,60], 
         [70,80,90]]

for j in list1:   # [10,20,30]
    for m in j:   # 10  20   30
        print(m,end=' ')   # 10 20 30 40 50 60 70 80 90 

print()

list2=[]
list3=[]
for i in range(len(list1)):   # 3          0  1
    list3 = []
    for j in range(len(list1[0])):  # 3    # 0 1 2  0 1 2
       list3.append(list1[j][i])
    list2.append(list3)

for x in list2:
    print(x)


# ----------------- New --------------------------------

# List Comprehension

list1 = [10,20,30,40,50,60]

for i in list1:
    print(i*i)

square = [(j*j) for j in list1]
print(square)  # [100, 400, 900, 1600, 2500, 3600]

cube = [(j*j*j) for j in list1]
print(cube)  # [1000, 8000, 27000, 64000, 125000, 216000]

# [(2,8), (10,1000), (5,125)]

cube_pair = [(_,_*_*_) for _ in list1]
print(cube_pair)  # [(10, 1000), (20, 8000), (30, 27000), (40, 64000), (50, 125000), (60, 216000)]

list1 = [90,902,3,3,5,5,63435]

for j in list1:
    print(j)

for k in range(len(list1)):
    print(list1[k])

list11 = [10,20,30,40,50,650]

# MAke combination of this list Ex. [(10,10), (10,20), (10,30)....]

list33 = [(i,j) for i in list11 for j in list11]
print(list33)

# [(10, 10), (10, 20), (10, 30), (10, 40), (10, 50), (10, 650), (20, 10), (20, 20), (20, 30), (20, 40), (20, 50), (20, 650), (30, 10), (30, 20), (30, 30), (30, 40), (30, 50), (30, 650), (40, 10), (40, 20), (40, 30), (40, 40), (40, 50), (40, 650), (50, 10), (50, 20), (50, 30), (50, 40), (50, 50), (50, 650), (650, 10), (650, 20), (650, 30), (650, 40), (650, 50), (650, 650)]

# freq = int(input())
# list40 = []
# for i in range(freq):
#     x = int(input())
#     if x % 2 != 0:
#         list40.append(x)
#     else:
#         pass

# print(list40)

# list55 = [int(i) for i in list1 if i % 2 != 0]
# print(list55)  # [3, 3, 5, 5, 63435]

# list55 = [int(i) for i in input().split()]
# print(list55)   # [34, 122, 56, 78, 90, 23, 11]

list45 = []


# dim = int(input("Enter Dimension: "))
# for i in range(dim):
#     list2d = [int(j) for j in input().split()]
#     list45.append(list2d)

# print(list45)  # [[10, 20, 30], [40, 60, 78], [34, 56, 78]]

print(-18 // 4)  # -5