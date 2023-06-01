def fibonnacci(num):
    n1,n2 = 0,1

    print(n1,n2,end=' ')

    for i in range(num-2):
        n3 = n1 + n2
        print(n3,end=' ')
        n1 = n2
        n2 = n3


# fibonnacci(5)

# Recursion ---> WHen function calls itself then it is called as Recursion

# Recursive Function
# print()
# print()

# from functools import lru_cache

# @lru_cache(maxsize=1000)
# def fibonacci_rec(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci_rec(num-1) + fibonacci_rec(num-2)
    
# # print(fibonacci_rec(6))  # 8
# print()
# print()


# for i in range(50):
#     print(fibonacci_rec(i),end=' ')


# H.w -> Factorial, 1 to 100 without using Loop

# -------------------------------------

# lambda Function
# Anounomus Fuction


def square(num):
    return num**2

print(square(20))   # 400
  

square1 = lambda x : x**2
print(square1(40))   # 1600


def sum(x,i,u):
    return x+i+u

print(sum(20,30,40))

calc = lambda x,i,u : x+i+u
print(calc("Marlin","Patel","Royal"))   # 610



# a * (x**2) + (b*x) + c

def quadratic_fun(a,b,c):
    return lambda x : a * (x**2) + (b*x) + c


Jay = quadratic_fun(10,20,30)
print(Jay(5)) # 380




def fibonacci_rec(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_rec(num-1) + fibonacci_rec(num-2)
    
import time

time_rec = time.time()
print(fibonacci_rec(6))  # 8
print("Total time of Recursive fun: ",time.time() - time_rec)


def fibo(num):
    list1 = [0,1]

    for i in range(num): 
        list1.append(list1[-1] + list1[-2])

    return list1[-2]

time_ite = time.time()
print(fibo(6))  # 8
print("Total time of Recursive fun: ",time.time() - time_ite)


square1 = lambda x : x**2
print(square1(40))   # 1600


list9 = [34,90,21,34,56]

# Map, Reduce, filter
res = map(lambda x : x**2, list9)  # <map object at 0x000001A9A987FD00>
res = list(map(lambda x : x**2, list9))  # <map object at 0x000001A9A987FD00>

print(res)   # [1156, 8100, 441, 1156, 3136]


# Recursive Function, Lambda, Map -> 10 Programs