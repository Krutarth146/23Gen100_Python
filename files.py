# Numpy, pandas, matplotlib, seaborn, csv, files, Exception Handling

# Files 

# Files types 1. Text File 't'  2. Binary File  'b'


# Modes

'''
'w' - Write Mode -> If file does not Exist then It will create new one. (Overwrite)
'r' - Read Mode  -> If file does not Exist then It will Generate an Error
'a' - Append Mode -> If file does not Exist then It will create new one. (Append the data to last line of code)
'x' - If file does Exist then It will Generate an Error

'+' - read + Write Both Operation


'''

v1 = open("vivek.txt","w")
v1.write("Hello Vivek Jiiiii!!\n")


list1 = ["Hello Shrutijii\n", "Hello Both of u khushi jiiiii\n", "Hello Vrajjjjj\n"]

v1.writelines(list1)
v1.close()


v2 = open("vivek.txt",'r')
print(v2.tell())   # 0
x = v2.read()
print(v2.tell())   # 86
print(x)

v2.seek(0) # Reset
print(v2.readline())  # Hello Vivek Jiiiii!!
print(v2.readline())  # Hello Shrutijii
print(v2.readline())  # Hello Both of u khushi jiiiii
print(v2.readline())  # Hello Vrajjjjj
print(v2.readline())  # 

v2.seek(12)
print(v2.readlines())  # ['Jiiiii!!\n', 'Hello Shrutijii\n', 'Hello Both of u khushi jiiiii\n', 'Hello Vrajjjjj\n']
v2.close()

# Append, x, +

# Pickle Module  

# import pickle  # one jpg read ----> write in another file

# pickle.dump()
# r1 = open("Amit.txt","rb")


