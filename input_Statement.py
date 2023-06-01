# int x;

# int , float, bool (True, False), complex (2 + 8j)

x = -9000
print(x)  # -9000
print(type(x))  # <class 'int'>

y = -34444444444444444444444.8
print(type(y))   # <class 'float'>

z = True
print(type(z))  # <class 'bool'>

_ = 45 + 3j   # (45 is Real Part and 3j is Imaginary Part)
print(_)  # (45+3j)
print(type(_))   # <class 'complex'>

_dhiraj_sir = 'T'
print(type(_dhiraj_sir))  # <class 'str'>

viraj = "Harsh"
print(type(viraj))  # <class 'str'>

jk = '45'
print(type(jk))   # <class 'str'>

# -----------------------------------

# Typecasting (to convert from one datatype to another datatype)

x = 90
print(float(x))   # 90.0

e = 89.67
print(int(e))   # 89  (Data Loss)

g = "45.23"
# print(int(g))  # Gives Error

print(int(float(g)))   # 45

f = 90
print(str(f))   # 90
print(type(str(f)))   # 90  # <class 'str'>


r = 'A'
print(ord(r))  # 65

h = 'z'   # A- Z -> 65 to 90,   a-z -> 97 to 122
print(ord(h))  # 122

k = 88
print(chr(k))  # X

# Ram

print(f"{chr(82)}{chr(97)}{chr(109)}")  # Ram

# printf("Enter any Number: ");
# scanf("%d",&s);

# s = input('Enter Number: ')
# # print("Entered Number is",s)
# print(s)


# num1 = input()   # default str
# num2 = int(input())   # defaulr str

# print(int(num1) + int(num2))   # 562

w = 89
q = 22
print(w+q)   # 110

print(f"Sum of {w} and {q} is {w+q}")
print(f"Sub of {w} and {q} is {w-q}")
print(f"Mul of {w} and {q} is {w*q}")
print(f"Div (float) of {w} and {q} is {w/q}")  # 4.045454545454546
print(f"Div (floor) of {w} and {q} is {w//q}")  # 4
print(f"remainder of {w} and {q} is {w%q}")    # 1

# Task
# 1. Take age as Input from user and check whether he eleigible for voting or not??
# 2. Calc
# 3. Five programs of Area
# 4. Simple Interest
# 5. Check whether the t=year is leap year or not??  -> 