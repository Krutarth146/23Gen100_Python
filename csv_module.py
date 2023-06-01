# Explore Random Module
# import random, os, requests

# print(random.randint(1,100))   # 42

#  CSV Module ---> Comma seprated Values
import csv
filename = 'heart.csv'

fields = []
rows = []

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)   # <_csv.reader object at 0x0000019EA431BBE0>

    print("Total No. of lines %d"%csvreader.line_num)  # 919
    fields = next(csvreader)
    print(fields)  # ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope', 'HeartDisease']
    for row in csvreader:
        rows.append(row)

    # print(rows)

    print("Total No. of lines %d"%csvreader.line_num)  # 919

    for row in rows[:10]:
        for col in row:
            print("%10s"%col,end=' ')
        print()


student = [
    {'Name' : "Jay Sir", 'roll' : 90, 'Address' : "Ahm"},
    {'Name' : "Eshrey Sir", 'roll' : 910, 'Address' : "Goa"},
    {'Name' : "Zafar Sir", 'roll' : 1190, 'Address' : "Nadiad"},
    {'Name' : "Dhiraj Sir", 'roll' : 190, 'Address' : "Dubai"},
]


fields1 = ["Name" , "roll", 'Address']

with open("student.csv", "w") as csvfile1:
    writer = csv.DictWriter(csvfile1, fieldnames = fields1)
    writer.writeheader()
    writer.writerows(student)

fields4 = ['Name', 'Subject', 'Marks']
subject = [
    ["Khushi", 'Python', 900],
    ["Khushi1", 'Python3', 900],
    ["Khushi2", 'Python5', 9300],
    ["Khushi3", 'Python2', 9200],
    ["Khushi34", 'Python', 9200],
]

with open("sub1.csv","w") as csvfile3:
    csvwriter1 = csv.writer(csvfile3)

    csvwriter1.writerow(fields4)
    csvwriter1.writerows(subject)
