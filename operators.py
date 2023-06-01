# opearors (Operator Precedence and Associativity)

# 1. Arithmetic Operators  +  -  *  /(float)  //(floor)  %(modulas)  **(power)

a = 90
b = 80
print(a*b)

x = 3
print(x**4)   # 3*3*3*3  # 81

# Assignment Operator  =  += -= *= /= //= %= <<= >>=

c = 30

c += 1   # c = c + 1 # 31
c %= 2   # 1
c ** 3   # 1
print(c)   # 1


# Bitwise O/p     &(a*b)    |(a+b)     ^(xor)(same=0)

print(23&56)

# Negation
print(~45)   # -46
print(~-90)  # 89

# Logical Operators   and   or   not

# num = int(input("ENter Number: "))



# ------------------------------
# _ = 1
# while _ < 101:
#     print(_,end=' ')
#     _+=1

_ = 100
while _ >= 1:
    if _ % 5 == 0 and (_ % 7 == 0 and _ % 10 == 0):   # 1   and 1
        print(_,end=' ')
    _-=1
# 70

# if num % 5 == 0 and num % 7 == 0:
#     print("Divisible by 5")
# else:
#     print("Fail")


# H.w.
# print 1 to 100 without using any loop (Don't use goto)
# Operator Precedence and associativity
# Negation
# Print Prime Numbers between 1 to 10000

# Negation
# print(~45)   # -46
# print(~-90)  # 89


# switch(choice)   # 'A'
# {
#     case 'A': print("Rishi")

#     case 'a': print("Viraj")
#                 break;
# }


choice = input()
match choice:
    case 1: print(1)

    case 'S': print("S")

    case "Viraj": print("VIraj")

    case "True": print(True)

    # case other: print("Invalid")
    case _: print("Invalid")

if choice == 'Viraj':
    print("Pass")
elif choice == 'S':
    pass