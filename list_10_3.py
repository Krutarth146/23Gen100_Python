list1 = [10, 90, 80, 78 , 77, 77, 78]

print(list1)  # [10, 90, 80, 78, 77, 77, 78]



# Power

# num = int(input())   # 5
# power = int(input())  # 2

# mul = 1
# for i in range(power):
#     mul *= num   # 5 * 5 = 25

# print(mul)  # 25

# print(num ** power)  # 25



str1 = "Krutarth Daxeshkumar Patel"

ans = 'K.D.Patel'

words = str1.split(' ')
# print(words)

print(f"{words[0][0]}.{words[1][0]}.{words[2][0:]}")



list1 = ["Harsh22222222222222222222", "Thakar", 'Patel123222222', 'Vivek111111']

max = 0
str1 = ''
for i in range(len(list1)):
    length = len(list1[i])  # 5
    if max < length:   # (0 < 5)
        max = length   # max = 5
        str1 = list1[i]

print(str1)



# -----------------------------------------

# Matrices

list1 = [[1,2,3], [4,5,6], [7,8,9]]

print(len(list1))  # 3

# for i in list1:
#     print(i)

# for _ in list1:  # _ = [4,5,6]
#     for h in _:  # h = 4
#         print(h,end=' ')  # 1 2 3 4 5 6 7 8 9


list2 = [[1,2,3], [4,5,6], [7,8,9]]
 # Make this User defined (Also Dimension) ----------------------
for i in range(len(list2)):  # 3   # 0 1 2
    if i % 2 == 0:
        for j in range(len(list2[0])):  # 3  # 0 1 2
            print(list2[i][j],end=' ')  # 0 2
    elif i % 2 != 0:
        for j in range(len(list2[0])-1,-1,-1):  # 3  # 0 1 2
            print(list2[i][j],end=' ')

    # Implement htis program using while loop ----------------------
    # row to col and col to row
    # Sum of Diagonal Elements
    # List, string Programs