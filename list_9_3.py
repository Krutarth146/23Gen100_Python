list1 = [10, 90, 89, 78, 67, 67]
print(list1)  # [10, 90, 89, 78, 67, 67]

# List is Mutable (Changeble), ordered(Indexed), Allow Duplicates

list1.append(900)  # None
print(list1)  # [10, 90, 89, 78, 67, 67, 900]

list1.append("Marlin")
print(list1)  # [10, 90, 89, 78, 67, 67, 900, 'Marlin']

list1[2] = "Zeel"
print(list1)  # [10, 90, 'Zeel', 78, 67, 67, 900, 'Marlin']

# list1.extend(900)  # Gives Error
list1.extend('900')  # Gives Error
print(list1)  # [10, 90, 'Zeel', 78, 67, 67, 900, 'Marlin', '9', '0', '0']

list1.extend("Viraj")
print(list1)  # [10, 90, 'Zeel', 78, 67, 67, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a', 'j']



list2 = [10, 980, 56, 34, 230]

# list1.extend(list2)
# print(list1)  # [10, 90, 'Zeel', 78, 67, 67, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a', 'j', 10, 980, 56, 34, 230]
# print(len(list1))  # 21

# list1.append(list2)
# print(list1)  # [10, 90, 'Zeel', 78, 67, 67, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a', 'j', [10, 980, 56, 34, 230]]
# print(len(list1))  # 17

list1.insert(3,"Devanshi")
print(list1)  # [10, 90, 'Zeel', 'Devanshi', 78, 67, 67, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a', 'j']

list1.insert(-1,"Harsh Takkar")
print(list1) # [10, 90, 'Zeel', 'Devanshi', 78, 67, 67, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a', 'Harsh Takkar', 'j']


list1.pop()
print(list1) # [10, 90, 'Zeel', 'Devanshi', 78, 67, 67, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a', 'Harsh Takkar']
list1.pop()
print(list1) # [10, 90, 'Zeel', 'Devanshi', 78, 67, 67, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a']

list1.pop(3)
print(list1) # [10, 90, 'Zeel', 78, 67, 67, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a']

list1.remove('Zeel')
print(list1)  # [10, 90, 78, 67, 67, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a']

list1.remove(67)
print(list1)


for i in list1:
    if i == 67:
        list1.remove(i)

print(list1)


list2 = [90, 89, 78, 67, 90, 89]

# Option - 1

# Set - Don't Allow Duplicates, Unordered, Immutable**

# set1 = {10, 90, 80 , 10, 10, 10}
# print(set1)  # {80, 10, 90}

# list2 = list(set(list2))
# print(list2)  # [89, 90, 67, 78]


# Option2

list9 = []  # 90, 80

for i in list2: # 90
    if i not in list9:
        list9.append(i)

print(list9)  # [90, 89, 78, 67]

# list1.clear()
# print(list1)   # []

print(list1.count('MaRlin'))   # 0
print(list1.index('r'))  # 10 # starts from 0

list1.reverse()
print(list1)  # ['a', 'r', 'i', 'V', '0', '0', '9', 'Marlin', 900, 78, 90, 10]

print(list1[::-1])  # [10, 90, 78, 900, 'Marlin', '9', '0', '0', 'V', 'i', 'r', 'a']


list1 = [10, 90, 89, 34, 56, 101]
list1.sort()
print(list1)  # [10, 34, 56, 89, 90, 101]

list1.sort(reverse=True)   # In decresing Order
print(list1) # [101, 90, 89, 56, 34, 10]




'''
Task-:
1. Create a list of Fruits(15 exotic fruits)
take user input and check if the fruits are avail in the list
if available print "fruit_name is Available"


2. create a list of numbers(15 numbers (1-100))
sort that list in ascending order
search for the number in the list
take input from user and find all the occurence
print the occurence


Tasks-: 
    1. Wap to find no. of month from the given no. of days
    2. wap to scan seconds and print hour, minute and remaining seconds
    3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    4. wap to check whether the number is odd or even
    5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    6. wap to make any user inputted string in uppercase or lowercase
    7. wap to print the sum of user entered numbers (scan by the user)
    8. wap to find power of a number
    9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
    Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

'''