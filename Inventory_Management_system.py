list1=  ['10','20','30','4']

x = list(map(int, list1))
print(x)   # [10, 20, 30, 4]

# Factorial    5 ---> 5*4*3*2*1


from functools import reduce
num = 8
res = reduce(lambda x,y:x*y, [i for i in range(1,num+1)])
print(res)   # 40320

ans = []
for i in range(1,num+1):
    ans.append(i)

print(ans)

# ----------------------------------

print("Inventory Management System")

# record = {'1001' : {'pName' : "Parle G", 'qn' : 340, 'price' : 5},
#          '1002' : {'pName' : "Oats", 'qn' : 120, 'price' : 30},
#          '1003' : {'pName' : "Kellogs", 'qn' : 22, 'price' : 50},
#          '1004' : {'pName' : "Cadbury", 'qn' : 300, 'price' : 25},}

import json   # Javascript Object Notation

f1 = open("record.txt",'r')
x = f1.read()
record = json.loads(x)
f1.close()

# print(dict1['1003']['price'])   # 50
# print(dict1['1002']['qn'])   # 50
# print(dict1['1002']['pName']['brand'])   # Adani
# print(dict1.get('1001'))


# print(record[0]['1001']['qn'])   # 340


print("------------Menus------------")
for i in record.keys():
    print(i, '---', record[i]['pName'], '||', record[i]['qn'], "||", record[i]['price'])


user_need = input("Enter Product Id: ")
quantity = int(input("Enter Product Quantity: "))

total_bill = 0
if quantity < 0:
    print("Please Enter Valid quantity.")
    exit()

if quantity <= record[user_need]['qn']:
    total_bill = quantity * record[user_need]['price']
    record[user_need]['qn'] -= quantity
    print("Your Bill Amount is",total_bill)
    print("Thank You! Inventory Updated.")

else:
    print(f"We have only {record[user_need]['qn']} Quantities.")
    temp = input("If you need then press y or Y: ")

    if temp.lower() == 'y':
        total_bill = record[user_need]['qn'] * record[user_need]['price']
        record[user_need]['qn'] = 0
        print("Your Bill Amount is",total_bill)
        print("Thank You! Inventory Updated.")
    else:
        print("Thank You Visit Again!")

import json   # Javascript Object Notation
fp = open("record.txt",'w')
js = json.dumps(record)
fp.write(js)
fp.close()


# Bill.txt  -----> Customer's Name, Date (datetime), total_bill
# .txt ---> .csv  ---> Formatting

print((3+4)//2+6)

import pandas as pd

df = pd.read_json(r'C:\Users\KRUTARTH\OneDrive\Desktop\Krutarth_Study\Python\Gen100\record.txt')
print(df)

df.to_csv('record.csv')