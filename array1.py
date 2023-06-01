import matplotlib.pyplot
import array
# import numpy

# from matplotlib import *
khushi = array.array('i',[1,8,3,4,56,6])

x = [10,20,30,40]
y = [34,56,78,32]
matplotlib.pyplot.plot(x,y)
print(matplotlib.pyplot.show())

print(khushi)  # array('i', [1, 8, 3, 4, 56, 6])

aman = array.array('f',[1,8,3,4,56,6])
print(aman)  # array('f', [1.0, 8.0, 3.0, 4.0, 56.0, 6.0])

harsh = array.array('u',['A','B','Z'])
print(harsh)
print(type(harsh))  # <class 'array.array'>


aman.insert(2,3900)
print(aman)


list1 = [10,20,390,40,60,800]
list2 = [45,89,32,23,11,900,900]

list3 = [(i,j) for i,j in zip(list1,list2)]
print(list3)  # [(10, 45), (20, 89), (390, 32), (40, 23), (60, 11), (800, 900)]

list4 = [34, 90, 78, 56]

list5 = [i for i in enumerate(list4)]
print(list5)   # [(0, 34), (1, 90), (2, 78), (3, 56)]

list5 = [[i,j] for i,j in enumerate(list4,100)]
print(list5)   # [[100, 34], [101, 90], [102, 78], [103, 56]]

list1=[(4,6), (1, 3), (6, 8), (4, 1), (5, 2)]
list2=[]
for i in list1:
    sub=abs(i[0]-i[1])
    if sub == 3:
        list2.append(i)
for i in list1:
    sub1=abs(i[0]-i[1])
    if sub1 == 2:
        list2.append(i)
print(list2)