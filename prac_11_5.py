# Car Parking
vehicles = 200   # 2w + 4w
wheels = 540

# 2w ??   4w??

# -----------------------------------------
list1 = [[10,67,21,10], [78,90,42,20], [78,54,21,30]]
# Find Second largest ELement from all lists.
# ans = [21,78,54]
# list2 = []
# for i in list1:
#     list2.append(sorted(i))

# print(list2)
# ans = []
# for i in list2:
#     ans.append(i[-2])

# print(ans)

# Map, reduce,filter 

ans_1 = list(map(lambda x:sorted(x)[-2],list1))
print(ans_1)


# --------------------------------------------

str1 = "oye balle balle oye"
ans1 = "OyE BallE BallE OyE"

list1 = str1.split(' ')
print(list1)