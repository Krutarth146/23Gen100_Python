str1 = 'Royal is Best institute Ever123.'

print(str1)  # Royal is Best institute Ever123.
str2 = "H"
print(type(str2))

list1 =[10,90,80.78,78]
tup1 = (30, 77.45, 'vdfv',77.45)

print(len(str1))  # 32  # start from 1, Index starts from 0
print(str1[-32])  # R
print(str1[0])  # R

str1 = 'Royal_is Best institute Ever123.'
print(str1[-4])  # 1


# Slicing
# print(str1[start : End(n-1)])
print(str1[0:6])  # start - 0, ENd - 5  # Royal_

print(str1[4:10])   # l_is B
print(str1[:10])   # Royal_is B
print(str1[4:])   # l_is Best institute Ever123.
# print(str1[start : end])
print(str1[0 : 5])
print(str1[ : ])  # Royal_is Best institute Ever123.
print(str1[10:3])  # blank

# print(str1[start : End(n-1)] : step(n-1))
print(str1[2:8:1])  # yal_is
print(str1[2::3])  # y_ situ e2
print(str1[10:6:3])  # blank
print(str1[1:6:])  # oyal_

print(str1[2:9:-1])  # blank
str1 = 'Royal_is Best institute Ever123.'
print(str1[12:9:-1])  # tse
print(str1[-4:-1:-3])  # blank
print(str1[-4:-10:-3])  # 1v
print(str1[-4::-3])  # 1vets eslo
print(str1[-4::3])  # 1.
print(str1[-5:2:3])  # blank

# STring Methods

str1 = '1RoyalisBestinstituteEver'
print(str1.capitalize())  # Royal_is best institute ever123.
print(str1.title())  # RoyalIs Best Institute Ever123.
print(str1.upper())  # ROYAL_IS BEST INSTITUTE EVER123.
print(str1.lower())  # royal_is best institute ever123.
print(str1.casefold())  # royal_is best institute ever123.
print(str1.swapcase())  # rOYAL_IS bEST INSTITUTE eVER123.

str2 = "DDDD DDD"
print(str2.isupper())  # True
print(str1.islower())  # False
print(str1.istitle())  # False
print(str1.isalnum())  # True
print(str1.isalpha())  # True
print(str1.isdigit())  # True
print(str1.isnumeric())  # True
print(str1.isdecimal())  # True
print(str1.isascii())  # True
print(str1.isprintable())  # True
print(str1.isidentifier())  # False

print(str2.count('DDDD'))  # 1
print(len(str2))  # 8
print(str2.center(25,'*'))  # 1
