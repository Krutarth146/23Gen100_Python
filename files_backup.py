'''
    # File ---> 1. Text File (t)   2. Binary File (b)

    Text file ---> \n  \t  \r  \b

    Binary FIle---> Image

    # File Opening Modes
    'w' --> Write Mode (Overwrite)

    'r' --> Read Mode (Need File)

    'a' --> Append Mode

    'x' --> If file Exists then It will generates an Error

    '+' --> Read + Write

'''
# FILE *fp;
fp = open("Harsh.txt","w")

fp.write("Hello My name is Krutarth\tPatel")


lines = ["\nHarsh Thakar\n", "Jay Nasriwala\n", "Devanshi Trivedi\n", "Vraj Shah\n"]

fp.writelines(lines)

fp.close()

num1 = 90
num2 = 800
num3 = 6700


maximum = lambda num1,num2,num3 : (print(num1) if num1 > num3 else print(num3)) if \
    num1 > num2 else (print(num2) \
                      if num2 > num3 else\
                          print(num3))
maximum(num1,num2,num3)


f1 = open("harsh.txt",'r')
# x = f1.read()
# counter =0 
# for j in f1.read():
#     print(j)
#     counter+=1

# words= x.split()

# print(words)

# for w in words:
#     if w.startswith("Tri"):
#         print(True)
print(f1.tell())
print(f1.readline())
print(f1.tell())
print(f1.readline())
print(f1.tell())
print(f1.readline())
print(f1.tell())
print(f1.readline())
print(f1.tell())
print(f1.readline())
print(f1.tell())
print(f1.readline())
print(f1.tell())   # 91

f1.seek(33)

print(f1.readlines())  # ['Harsh Thakar\n', 'Jay Nasriwala\n', 'Devanshi Trivedi\n', 'Vraj Shah\n']
f1.close()
# print(x)
# print(counter)  # 86


i1 = open("car.jpeg","rb")
x = i1.read()
print(x)
i1.close()


i2 = open("Devanshi_car.jpeg","wb")
i2.write(x)
i2.close()


# Task

# Find TOtal words, characters, startswith s and a , endswith y, count of 'aeiou'
# Prime.txt, armstrong.txt