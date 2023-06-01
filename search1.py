# RE, DB, GUI

list1 = [10,90,89,78,56,34]

need = 110
# Linear Search
for j in list1:
    if j == need:
        print("Element is Found")
        break
else:
    print("Element is Not Found")


# Binary Search

list2 = [i for i in range(1,101)]

print(list2)

start = 0  # start = 0
end = len(list2) - 1 # End = 99

counter_binary = 0
# Binary Search
while start <= end: 
    counter_binary+=1
    mid = (start + end) // 2   # mid = 49
    if list2[mid] == need:
        print("Element is Found Binary")
        break

    elif list2[mid] < need:
        start = mid+1

    elif list2[mid] > need:
        end = mid-1
else:
    print("Not Found")

print(counter_binary)


a = 90
b = 8000
c = 6700

# lambda Max ??


# print(a) if a > b else print(b)
Greater = lambda a,b,c : (print(a) if a > c else print(c)) if a > b else (print(b) if b > c else print(c))
Greater(a,b,c)



x = 90

def modify():
    global x
    x+=10
    print(x)

modify()   # 50
print(x)   # 90


# Anagram [] 

# Panagram  # [] --> A to Z



list2d = [[90,54,20], 
          [4,67,21], 
          [89,65,2]]