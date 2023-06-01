# Function (4 Types, Default Func., Global - local, *args - **kwargs, Recursion,
# lambda, nested lambda, map, reduce, filter, accumulate)


def khushi(n1,n2,n3=10):
    return n1 + n2 + n3

print(khushi(10,78))

# ---------------------------------

num = 90

ans = lambda x : x**2

print(ans(num))  # 8100

# ----- Nested Lambda

res = lambda x  : lambda \
    n1, n2 : \
        x ** n1 + n2 

# rohan = res()

# print(rohan(2,2))  # 102

print(res(10)(4,9))  # 10009


# Regular Expression RE
# GUI
# mysql DB Connection
# NLP (Natural Lang. Processing  1. Speech Recognization  2. Text Recognization)

# REGEX  ---> Vraj Kraj Mraj Graj
# CSV


# Dictionary Comprehension

dict1 = [10,90,89,{'Name' : "Rohan" , 'address' : {'country' : "India", 'state' : "Gujarat", 'Area' : {'Main' : "GNR", 'sub' : "Sarghasan", "Pincode" : [390001, 88888, 66666, 455322]}} }]
 
value = dict1[3]['address']['Area']['Pincode'][1]
print(value)  # 88888


l1 = [90,67,35,72]

cube = {x : x**3 for x in l1}
print(cube)  # {90: 729000, 67: 300763, 35: 42875, 72: 373248}

str2 = "Viraj"

# {'V' : 'vv' , 'I' : 'ii' .....}

name = "Harsh"
split_name = list(name)

result = []
for char in split_name:
    result.append(char.upper())
    result.append(char.lower() * 2)

print(result)

str1="jay"

j={i.upper() : i.lower()*2 for i in str1}
print(j)

#  ------------------

dict1 = {
    'list1' : [10,90,89,67],
    'list2' : [67,34,21,65],
    'list3' : [33,90,86,51]
}

# {'list1' : 256, 'list2' : 900...}
print({x: sum(dict1[x]) for x in dict1})   # {'list1': 256, 'list2': 187, 'list3': 260}
