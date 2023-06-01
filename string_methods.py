str1 = "Royal_Is Best institue Ever123."

print(str1.capitalize())  # Royal_is best institue ever123.
print(str1.casefold())  # royal_is best institue ever123.
print(str1.swapcase())  # rOYAL_IS bEST INSTITUE eVER123.
print(str1.title())    # Royal_Is Best Institue Ever123.
print(str1.upper())    # ROYAL_IS BEST INSTITUE EVER123.
print(str1.lower())    # royal_is best institue ever123.

# 65 to 90 - A to Z
# 97 to 122 - a to z

# b - 98
# B - 66

print(len(str1))   # 31
print(str1.center(40,'*'))  # ****Royal_Is Best institue Ever123.*****

print(str1.count("i"))  # 2
print(str1.count("I"))  # 1
print(str1.lower().count("i"))  # 3



# str2 = ""
for i in range(len(str1)):  # 0 to 30
    if str1[i]=='t':   # t == t
        # print(str1[i])   # t
        print(str1[i].upper(),end='')   # T  # Gives Error
    else: 
        print(str1[i],end='')

print()

str1 = "Royal_Is Best institue Ever123."

print(str1.count(" ",0,9))  # 2
print(str1.count("sI",0))  # 0

print(str1.encode())  # b'Royal_Is Best institue Ever123.'

# Hello, I am Krutarth
# rrffq, s dv fvdfvdvf

str2 = "Ståle"
print(str2.encode())  # b'St\xc3\xa5le'

print(str2.encode(encoding="ASCII",errors='namereplace')) # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str2.encode(encoding="ASCII",errors='replace')) # b'St?le'
print(str2.encode(encoding="ASCII",errors='ignore')) # b'Stle'
print(str2.encode(encoding="ASCII",errors='xmlcharrefreplace')) # b'St&#229;le'
print(str2.encode(encoding="ASCII",errors='backslashreplace')) # b'St\xc3\xa5le'
print(str2.encode(errors='greek')) # b'St\xc3\xa5le'
print(str2.encode(errors='latin')) # b'St\xc3\xa5le'

print(str1.endswith('3.'))  # True

str1 = "Royal_Is Best institue\tEver123."
print(str1.expandtabs(16))


# print(str1.find('Z'))  # -1   if string is Not found then it will return -1.
# print(str1.index('Z')) #  if string is Not found then it will Generate Error.


# str2 = "{name} is {mode} Boy.".format(name="Henish", mode="Good")
# str2 = "{} is {} Boy.".format("Kaushal", "Good1")  # Kaushal is Good1 Boy.
str2 = "{1} is {0} Boy.{2}".format("Kaushal" , "India", "Good1")  # India is Kaushal Boy.Good1
print(str2) 

x = 90
y = 80

print(x,'+',y,'=',x+y)  # 90 + 80 = 170  
print(f"{x} * {y} = {x*y}")  # 90 * 80 = 7200   # fstring


name = "Marlin"
college = "Silver Oak University"
print(f"{name} is studying in {college} now.")  # Marlin is studying in Silver Oak University now.


dict1 = {"Address_1" : "Ahm", "role" : "Python developer", "Address_1" : "Patna", "Age" : [21,45,67,23], 4: [12,3,4,4]}
# dict2 = {"Age" : "Aanand"}
# dict1.update(dict2)
# print(dict1)  # {'Address': 'Patna', 'roll': 'Python developer'}
str3 = "Khushi lives in {Address_1} and her role is {role} +  {Age}."
print(str3.format_map(dict1))  # Khushi lives in Patna and her role is Python developer.

print(len(dict1))   # 4
print(dict1.keys())  # dict_keys(['Address', 'role', 'Age', 'city'])
# print(dict1[3])  # Gives Error

# for i in dict1.values():
#     if type(i) == list:
#         for j in i:
#             print(j)

str2 = "    "

# print(str2.index('G'))  # 9
print(str2.isalnum())   # True
print(str2.isalpha())   # False
print(str2.isascii())   # True
print(str2.isdecimal())  # True
print(str2.isdigit())     # True
print(str2.isnumeric())   # True

print(str2.islower())   # False
print(str2.isidentifier())   # True
print(str2.isprintable())  # True
print(str2.isspace())   # False



str2 = "Morning, Royal_techno Best Techno Institute Techno Ever"
str1 = ' '.join(str2)
print(str1)  # M o r n i n g ,   R o y a l   T e c h n o

print(len(str2))   # 21
print(str2.ljust(25,'*'))  # Morning, Royal Techno****
print(str2.rjust(25,'*'))  # ****Morning, Royal Techno

str3 = "Devanshi"

# str2 = str2 + ' ' + str3
print(str2)  # Morning, Royal Techno Devanshi

print(str2.lower())  # morning, royal techno devanshi

print(str2.lstrip())  # Morning, Royal Techno
print(str2.rstrip())  #         Morning, Royal Techno
print(str2.strip())  # Morning, Royal Techno

print(str2.partition('Techno')) # ('Morning, Royal ', 'Techno', ' Best Techno Institute Ever')  # DIvides into 3 Parts only
print(str2.rpartition('Techno')) # ('Morning, Royal Techno Best ', 'Techno', ' Institute Ever')

print(str2.removeprefix('M'))  # orning, Royal Techno Best Techno Institute Ever
print(str2.removesuffix('r'))  # Morning, Royal Techno Best Techno Institute Eve

print(str2.replace('Techno', 'Technosoft'))  # Morning, Royal Technosoft Best Technosoft Institute Ever
print(str2.replace('Techno', 'Technosoft'))  # Morning, Royal Technosoft Best Technosoft Institute Ever

print(str2.find('e'))   # 16
print(str2.rfind('e'))   # 46

print(str2.split('Techno'))  # ['Morning, Royal ', ' Best ', ' Institute ', ' Ever']

print(str2.title())  # Morning, Royal_Techno Best Techno Institute Techno Ever

str5 = 'dvfdf188'
print(str5.zfill(20))  # 00188

str6 = "Hello Yash"

table = str6.maketrans('Yash',"Hars","Hello")
print(table)  # {89: 72, 104: None}


str6 = str6.translate(table)
print(str6)  # Hello Has


# String Programs

# 1. Write a Py program that takes your full Name and Print Like This :
# Input - Krutarth Daxeshbhai Patel
# o/p   - K.D.Patel

# 2. Find NUmber of spaces characters in a given str.
# input - Python Programming

# o/p - vowels - 4, white spaces - 1, consonents - 13

# 3. write a py program to make a new string
# input  - This is the lion in the cage.
# o/ p - This is lion in cage.

# 4. WAP:
# input - Keep yourself Mute while not speaking
# output - Keep_yourself Mute while not#speaking

# 5. Write a program to calculate the sum of series up to n term. For example, if n = 5 the series will become 3 + 33 + 333 + 3333 + 33333 = ???

# 6. Write a Python function that checks whether a passed string is palindrome or not.

# 7. Write a Py program to calculate the factorial of a number (a non-negative integer).

# 8. Python program to find second largest number in a list.  // Null
