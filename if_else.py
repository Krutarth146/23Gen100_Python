# Age Eligibility
# name = input("ENter Name: ")
# age = int(input("Enter age: "))

# # if()
# # {

# # }
# # else
# # {

# # }

# if age >= 18:
#     print(f"{name} is eleigible for voting.")
# else:
#     print("Not Eligible for voting")


# Take days as input from user and calculate total no. of year, month, remaining days.

# Ex. 400 -> 1 year, 1 month, 5 remaining days

# days = int(input("Enter total days: "))  # 400

# year = days // 365  # 1
# month = (days % 365) // 30    # 1
# rem_days = (days % 365) % 30

# print(f"Total years = {year}, month = {month}, remaining_days are {rem_days}")

# Take seconds as input from user and find total hours, minutes, and remaing seconds


num = 10   # Assignment Operator

if num < 0:
    print("Negative")
elif num == 0:   # Equality Operator (Comparison)
    print("zero")
else:
    print("Positive")



# ---------------------------

a = 90
b = 80

if a > b:
    print("90 is Bigger")
else:
    print("80 is bIgger")


a = 90
b = 780
c = 5600

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)


# printf("%d",(  a > b ? ((a > c) ? a : c) : ((b > c) ? b : c) ));

print(a if a > b else b) # hw, seconds, last , 
# hw -> Take 3 subjects marks as input, and calculate total and avg. if avg is bw 100 to 80 then a grade, 80 to 60 - b grade and 40 to 60 -> c grade and Under 40 -> fail, another condition is that pass in all 3 subject is required