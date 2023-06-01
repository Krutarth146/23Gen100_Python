# Function -> Code Reusability

# Function Syntax

# 1. Func. Defination
# 2. Func. Calling


# Func. Types (4)

# 1. without Return Type and Without args
# 2. w/o return type and with args
# 3. with return Type and w/o args
# 4. with return type and with args


# 1. without Return Type and Without args


def devanshi():   # Func. Defination
    print("Devanshi Trivedi")

devanshi()  # Func. Calling


# 2. w/o return type and with args

def khushi(viraj, jay, marlin):
    print(viraj + marlin + jay)

print(khushi(30,89,21.90))  # None


# 3. with return Type and w/o args

def vraj(devanshi:int, list1 = []):
    list1.append(devanshi)
    return list1

print(vraj(20))  # [20]

x = vraj(80)
print(x)  # [20, 80]


# int main()
# {

#     return 0;
# }


# 4. with return type and with args

def _Jay(x,y,z,w):
    return x,y,z,w

print(_Jay(10,20,30,22))  # (10, 20, 30, 40)



# ------------------
# Default Function
def Kru1(num1, num2, num3 =21):
    return num1 + num2 + num3


print(Kru1(20,40))   # 21

def royal(str1 , str2, str3=None):
    return str1 + str2

print(royal("Kru","tarth"))



# Args -----------------------

def vivek(*argssdcvnsdvbs):
    print(type(argssdcvnsdvbs))   # <class 'tuple'>
    for h in argssdcvnsdvbs:
        print(h,end=' ')

vivek(10,90.90,"kapil")   # 10 90.9 kapil


def meet(a,b,c,*args,k=56):
    print(type(args))   # <class 'tuple'>
    for h in args:
        print(h,end=' ')

    print(args)  # ('ahm', 90, 89)

meet(10,90.90,"kapil","ahm", 90,89)   # ahm 90 89


# kwargs

def samsung(*royal, **kwargs):
    print(kwargs)     # {'name': 'Manoj', 'roll': 500, 'address': ['Ahm', 'Gnr']}
    print(type(kwargs))  # <class 'dict'>

    for k in kwargs.values():
        print(k)
    for k in kwargs.items():
        print(k)


samsung(10,20,30,40,50,name="Manoj", roll = 500, address = ["Ahm", "Gnr"])


tup1 = ((10,20,30), (90,89,78))

list1 = []
for i in tup1:
    for g in i:
        list1.append(g)

list1.sort()

print(list1)


# Doubt: A python program to sort a tuple with nested tuple.
# Eg:((12,"lreve",89),(11,"aferf",44),(15,"dw3fg",35))
# index sort:2
# output: ((15,"dw3fg",35),(11,"aferf",44),(12,"lreve",89))


tup1 = ((12,"lreve",89),(11,"aferf",44),(15,"dw3fg",35))

list1 = []
for i in range(0,len(tup1)-1):
    if tup1[i][2] > tup1[i+1][2]:
        list1.append(tup1[i+1])
        list1.append(tup1[i])
    else:
        list1.append(tup1[i])
print(tuple(list1))