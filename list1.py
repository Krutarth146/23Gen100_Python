# array:

# int a[9];

list1 = [12, 90, 89, 78, 6756]
print(list1)  # [12, 90, 89, 78, 6756]
print(type(list1))  # <class 'list'>

list2 = [10, 90.89, 10, True, 'D', "Devanshi", [1,2,3,4,1,2], (1,32,4,1,4), {2,3,3}, 90+8j]
list3 = [10, 90.89, 10, True, 'D', "Devanshi", [1,2,3,4,1,2], (1,32,4,1,4), {2,3,3}, 90+8j]
print(list2)  # [10, 90.89, 10, True, 'D', 'Devanshi', [1, 2, 3, 4, 1, 2], (1, 32, 4, 1, 4), {2, 3}, (90+8j)]
print(type(list2))  # <class 'list'>

# List characteristics: Allow Duplicates, Ordered (Indexed), Mutable (Changeble)

print(list2[3])   # True
print(list2[-1])   # (90+8j)
print(list2[2:6:2])   # [10, 'D']
print(list2[-2:-5:2])   # []
print(list2[-2:-5:-2])   # [{2, 3}, [1, 2, 3, 4, 1, 2]]

list5 = [10,20.90]
print(list5.__sizeof__) # <built-in method __sizeof__ of list object at 0x0000023E9180E000>
print(list5.__sizeof__()) # 56
print(list2.__sizeof__())  # 120
print(list3.__sizeof__())  # 120
print(id(list2))    # 2101860775680
print(id(list3))    # 2101861103680
print(len(list2))   # 10  # Length start from 1, Index starts from 0

list3 = list2   # Deeep Copy

print(id(list2))    # 2037142009600
print(id(list3))    # 2037142009600


list4 = list2.copy()   # shallow Copy
print(id(list2))    # 1995908527872
print(id(list4))    # 1995912830784

list1.append(20)
print(list1)  # [12, 90, 89, 78, 6756, 20]

list1 = [(1,2,3,4,5), (5,3,3,2), (2,232,4,4)]

for outer in list1:
    # print(j, end= ' ')  # (1, 2, 3, 4, 5) (5, 3, 3, 2) (2, 232, 4, 4)
    for inner in outer:
        print(inner,end=' ')  # 1 2 3 4 5 5 3 3 2 2 232 4 4

print()
for i in range(len(list1)):   # 3   -> 0 1 2    , i=0
    for k in range(len(list1[i])):  # 5  -> 0 1 2 3 4  -> k=0
        print(list1[i][k],end=' ')   # list1[0]  list1[1]....  # 1 2 3 4 5 5 3 3 2 2 232 4 4


print(list1[2][1])  # 232