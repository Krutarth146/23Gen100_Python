dict1 = {}
print(type(dict1))   # <class 'dict'>

set1 = {10}
print(type(set1))   # <class 'set'>

dict1 = {'Name' : "Rishita", 'Roll' : 900, 89 : [10,20,30,90], 'marks' : 900, 'Active' : True, 'Name' : "Vraj"}

print(dict1)  # {'Name': 'Vraj', 'Roll': 900, 89: [10, 20, 30, 90], 'marks': 900, 'Active': True}

# Dictionary -> Keys -> Unique, values -> Allow's Duplicates, Mutable (Changeble)

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

print(len(dict1))   # 5

print(dict1.__sizeof__())  # 344
print(id(dict1))  # 3078841285632

# dict1.clear()
# print(dict1)  # {}

# del dict1
# print(dict1)

dict2 = dict1.copy()   # shallow copy
dict3 = dict1          # Deep Copy


dict3.update({"mobile" : 90212121})

print(dict1)   # {'Name': 'Vraj', 'Roll': 900, 89: [10, 20, 30, 90], 'marks': 900, 'Active': True, 'mobile': 90212121}


list1= [[]] * 3
list1[1] = 5
print(list1)  # [[], 5, []]

print(dict1['Name'])  # Vraj
print(dict1['Roll'])  # 900

dict1['marks12'] = 900
print(dict1)  # {'Name': 'Vraj', 'Roll': 900, 89: [10, 20, 30, 90], 'marks': 900, 'Active': True, 'mobile': 90212121, 'marks12': 900}

dict1['Roll'] = 2500
print(dict1)  # {'Name': 'Vraj', 'Roll': 2500, 89: [10, 20, 30, 90], 'marks': 900, 'Active': True, 'mobile': 90212121, 'marks12': 900}


print(dict1.get('Roll'))  # 2500
print(dict1['Roll'])      # 2500

print(dict1.keys())  # dict_keys(['Name', 'Roll', 89, 'marks', 'Active', 'mobile', 'marks12'])
print(dict1.values())  # dict_values(['Vraj', 2500, [10, 20, 30, 90], 900, True, 90212121, 900])
print(dict1.items())  # dict_items([('Name', 'Vraj'), ('Roll', 2500), (89, [10, 20, 30, 90]), ('marks', 900), ('Active', True), ('mobile', 90212121), ('marks12', 900)])


for i in dict1:
    print(i)

for i in dict1.keys():
    print(i)

for i in dict1.values():
    print(i)

for i in dict1.items():
    print(i,end=' ')  # ('Name', 'Vraj') ('Roll', 2500) (89, [10, 20, 30, 90]) ('marks', 900) ('Active', True) ('mobile', 90212121) ('marks12', 900)

for key, value in dict1.items():
    print(f"{key} ----- {value}")


str1 = "Mississippi"
ans = {'M' : 1, 'i' : 4, 's' : 4, 'p' : 2}