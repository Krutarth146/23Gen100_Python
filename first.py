# Single Line Comment

'''
Multi
Line
Comment
'''

# Python Interpreter     1. Code runner  2. Python

print('Hello Marlin')   # Hello Marlin


print("Rishi Chauhan",end='\n')   # default
print("Royal Technosoft",end=' Vivek ')
print("Helloji")   # Royal Technosoft Vivek Helloji
print("Good Night")

# --------------------------------------------------
print("Devanshi","Vraj",'f','Shruti', sep=' ')  # Devanshi Vraj f Shruti (' ')default
print("Devanshi","Vraj",'f','Shruti', sep=' Jay ')  # Devanshi Jay Vraj Jay f Jay Shruti


print('''
    Address: Royal Technosoft
             Pramukh Tengent
             Sargasan
             Gnr-90.
''')


    # Address: Royal Technosoft
    #          Pramukh Tengent
    #          Sargasan
    #          Gnr-90.


# printf("Sum of a and b is %d",sum);
print("Royal is Best Institute Ever",30,"Vivek Prajapati",900)  # Royal is Best Institute Ever 30 Vivek Prajapati 900

x = 90
y = 80

print("Sum of x and y is x+y")  # Sum of x and y is x+y

print("Sum of",x,"and",y,"is",x+y)  # Sum of 90 and 80 is 170
# or
print(f"Sum of {x} and {y} is {x+y}")  # Sum of 90 and 80 is 170  (fstring)
print(f"Sub of {x} and {y} is {x-y}")  # Sum of 90 and 80 is 10  (fstring)
print(f"Mul of {x} and {y} is {x*y}")  # Sum of 90 and 80 is 7200  (fstring)
print(f"Div(FLoat) of {x} and {y} is {x/y}")  # Sum of 90 and 80 is 1.125  (fstring)
print(f"Div(FLoor) of {x} and {y} is {x//y}")  # Sum of 90 and 80 is 1  (fstring)