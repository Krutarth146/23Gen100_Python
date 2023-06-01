# Map, Reduce, filter

# Map ---------------

list1 = [10,20,30,40,50]

square = lambda x : x ** 2

print(square(20))  # 400

list2 = list(map(lambda x : x ** 2, list1))
print(list2)  # [100, 400, 900, 1600, 2500]

str3 = ['34', '21', '90', '56']
marlin = tuple(map(lambda x : int(x), str3))

# print(marlin)  # <map object at 0x0000024FC9372650>
print(marlin)

# ------------------------
# function, Oops, list, tuple, dictionary, lambda, Exception Handling, files


# filter -------------------

lst3 = [40,50,690,10,20,80,190,35,5]


import statistics
lst5 = list(filter(lambda x : statistics.mean(lst3) < x, lst3))
print(statistics.mean(lst3))
print(lst5)

# lst9 = list(map(lambda t : t % 7 == 0, lst3))  # [False, False, False, False, False, False, False, True]
# lst9 = list(filter(lambda t : t % 7 == 0, lst3))  # [False, False, False, False, False, False, False, True]
lst9 = list(filter(lambda t : t **2 <= 1000, lst3))  # [False, False, False, False, False, False, False, True]
print(lst9)   # 35

# reduce -----------------------
list30 = [1,2,3,4,5,6]
from functools import reduce
ridham = (reduce(lambda d, w: d*w, list30))  # 720

print(ridham)  # 1120

from itertools import accumulate

r1 = list(accumulate(list30, lambda d, w: d*w))
print(r1)  # [1, 2, 6, 24, 120, 720]