# # Write a program to check if the letter ‘j’ is present in the word 'Python'.

# str1 = 'Pythonj'

# user_req = 'j'
# if user_req in str1:
#     print("It is Present")
# else:
#     pass


# # Write  a  program  to  check  if  the  word  'python'  is  present  in  the  "This  is  python programming lab".

# str2 = "This  is  python programming lab"
# user = "Python"

# if user in str2:
#     print("Available")


# ------------------- Tuple ---------------------------

list1 = [10,20,30]
tup1 = (10,20,30)

list2 = ()
print(type(list2))  # Tuple

print(list1.__sizeof__())   # 72
print(tup1.__sizeof__())    # 48   # Storage Efficient

print(len(tup1))   # starts from 1


tup2 = (10, 90, 78.67, 89+9j, 'V', "Marlin", True, {89,12,90,90,90}, {"name" : "Vraj", 'Roll' : [10,20,30,40], 28 : 'age'}, (10,20,10,10), [20,30,40,40], 89+9j, 90)
print(tup2)


# Tuple  -> Allow Duplicates, Ordered (Indexed), Immutable (Not Chnageble)


print(tup2[2])  #  78.67
print(tup2[-5])  # {89, 90, 12}

print(tup2[-3:4:3])  # ()
print(tup2[-3:4:-3])  # ((10, 20, 10, 10), True)

print()

# Tuple Methods

print(tup2.count(90))  # 2
print(tup2.index(89+9j))  # 10



tup2 = list(tup2)
print(type(tup2))  # <class 'list'>

tup2.append("Devanshi")

print(tuple(tup2))


tup3 = (10,20,50,60,30,40)

for i in sorted(tup3):
    print(i)


# tup3[2] = 90  # Gives Error


tup9 = ((10,20,30) , 
        (30,90,89), 
        (23,34,56))


# for i in range(len(tup9)):
#     for j in range(len(tup9[0])):
#         print(tup9[i][j])

# for i in tup9:
#     for j in i:
#         print(i)


'''
Tasks in tuple -: 

1. Python program to find the size of a tuple
-> tuple = ("python", "includehelp", 43, 54.23)

2. Python program for adding a Tuple to List and Vice-Versa
-> tuple = ("python", "includehelp", 43, 54.23)

3. Python program to find the maximum and minimum K elements in a tuple
-> 
Input: 
myTuple = (4, 2, 5,7, 1, 8, 9), k = 2

Output: 
(9, 8) , (1, 2)

4. Python program to create a list of tuples from given list having number and its cube in each tuple
->
Input: 
list = [4, 1, 6, 2]

Output: 
[(4, 64), (1, 1), (6, 216), (2, 8)]

5. Python program to remove all tuples of length K
-> 
Input:
[(1, 4), (2), (4,5,6,8), (26), (3, 0, 1), (4)] k = 1

Output:
[(1, 4), (4, 5, 6, 8), (3, 0, 1)]

6. Python program to extract digits from tuple list
->
Input: 
list = [(4, 62), (2, 65), (5, 9), (0,1)]

Output:
[4, 6, 2, 5, 9, 0, 1]

7. Python program to find all pairs combination of two tuples
->
Input:
tup1 = (1, 2), tup2 = (5, 7)

Output:
[(1, 5), (1, 7), (2, 5), (2, 7), (5, 1), (5, 2), (7, 1), (7, 2)]

8. Python program to join tuples if similar initial element
->
Input:
list = [(1, 4), (3, 1), (1, 2), (4, 2), (3, 5)]

Output:
list = [(1, 4, 2), (3, 1, 5), (4, 2)]






9. Python program to sort a list of tuples by second item
->
Input:
[(2, 5), (9, 1), (4, 6), (2, 8), (1, 7)]

Output:
[(9, 1), (2, 5), (4, 6), (1, 7), (2, 8)]

10. Python program to sort a list of tuples in increasing order by the last element in each tuple
-> tupList =[(5, 7), (12, 4), (20, 13), (45, 2)]

11. Python program to sort tuples by frequency of their absolute difference
-> 
Input:
[(4,6), (1, 3), (6, 8), (4, 1), (5, 2)]

Output:
[(4, 1), (5, 2), (4, 6), (1, 3), (6, 8)]

12. Python program to remove duplicate tuples irrespective of order
->
Input:
tupList = [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4), (9, 2)]

Output:
[(1, 2), (5, 7), (4, 6), (2, 9)]

13. Python program to order tuples by list
->
Input:
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

Output:
[('l', 5), ('a', 1), ('k', 2), ('e', 6)]

14. Python program to concatenate maximum tuples
->
Input:
tupList = [("python", 7), ("learn" , 1), ("programming", 7), ("code" , 3)]

Output:
"python programming"

15. Python program to flatten tuple of lists to a tuple
->
Input:
([4, 9, 1], [5 ,6])

Output:
(4, 9, 1, 5, 6)
'''

# 11. Python program to sort tuples by frequency of their absolute difference
# -> 
# Input:
# [(4,6), (1, 3), (6, 8), (4, 1), (5, 2)]

# Output:
# [(4, 1), (5, 2), (4, 6), (1, 3), (6, 8)]


# 13. Python program to order tuples by list
# ->
# Input:
# tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

# Output:
# [('l', 5), ('a', 1), ('k', 2), ('e', 6)]


tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)]
sortList = ['l', 'a', 'k', 'e']

# for i in sortList:


# Python program to concatenate maximum tuples
# ->
# Input:
# tupList = [("python", 7), ("learn" , 1), ("programming", 7), ("code" , 3)]
# Output:
# "python programming"

# 11. Python program to sort tuples by frequency of their absolute difference
# -> 
# Input:
# [(4,6), (1, 3), (6, 8), (4, 1), (5, 2)]

# Output:
# [(4, 1), (5, 2), (4, 6), (1, 3), (6, 8)]

# Input:
test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

# Output:
ans = [(5, 6, 7), (6, 8, 10), (7, 13)]

res = []
for sub in test_list:  # (5, 6)
    if res and res[-1][0] == sub[0]:
        print("if",res)
        res[-1].extend(sub[1:])
    else:
        print('else: ',res)
        res.append([ele for ele in sub])
res = list(map(tuple, res))
 
# printing result
print("The extracted elements : " + str(res))


test_list = [(1, 6), (11, 3), (9, 1), (6, 11), (2, 10), (5, 7)]
sub_diff1 = [5,8,8,5,8,2]

ans =       [(5, 7), (1, 6), (6, 11), (11, 3), (9, 1), (2, 10)]
sub_diff2 = [2,5,5,8,8,8]
# printing original list
print("The original list is : " + str(test_list))
 
# getting differences pairs
diff_list = [abs(x - y) for x, y in test_list]
print(diff_list)

res = sorted(test_list, key = lambda sub: diff_list.count(abs(sub[0] - sub[1])))

a = lambda sub: diff_list.count(abs(sub[0] - sub[1]))

print(res)
