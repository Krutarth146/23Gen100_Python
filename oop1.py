# OOPs ----> Object Oriented Programing

# structure ----> User Ddefined Datatype


# class Student
# {
#     int id;
#     char name[10];
#     float marks;

#     void set_data(int id, char name[], float marks)
#     {
#         this->id = id;
#         this->name = name;
#         this->marks = marks;
#     }

#     void display()
#     {
#         cout<<id<<name<<marks;
#     }
# };



# main()
# {
#             int    a;
#     struct Student marlin
# }

# Constructor ---> Solves the Intialization Problem

# self == this pointer in CPP, JAVA


# ----------------------------------------------------------------------
# Varibales ---> 1. Instance Variable  2. Class Variable

class Bank:
    ROI = 4   # class Variable

    def __init__(self, name):   # Constructor
        self.name = name   # Instance Variable
        self.balance = 0   # Instance Variable

    def deposit(self, money):
        if money > 0:
            self.balance += money

    def withdraw(self,money):
        if money <= 0 or (self.balance - money) <= 5000:
            print("Not Allowed")
        else:
            self.balance -= money

    def check_bal(self):   # Instance Method
        print(f"Your Bal is {self.balance}")

    @classmethod
    def increase_ROI(cls):
        cls.ROI += 2

    @staticmethod
    def locker():
        pass

    def calculate_Interest(self):
        self.balance += (self.balance * Bank.ROI) / 100
        print("Interst Calculated!")


marlin = Bank("Marlin")
viraj = Bank("Viraj")

print(marlin.ROI)  # 4
print(viraj.ROI)  # 4
print(Bank.ROI)  # 4
# print(Bank.name)  # Error


viraj.deposit(10000)
viraj.withdraw(8000)
viraj.withdraw(2000)
viraj.check_bal()
# Bank.increase_ROI()
viraj.increase_ROI()
viraj.calculate_Interest()
viraj.check_bal()  # Your Bal is 8480.0


marlin.deposit(40000)
marlin.withdraw(38000)
marlin.withdraw(5000)
marlin.check_bal()
# Bank.increase_ROI()
marlin.increase_ROI()
marlin.calculate_Interest()
marlin.check_bal()  # Your Bal is  37800.0

marlin.address = "Gnr"
print(marlin.address)  # Gnr
# print(viraj.address)  # Error

marlin.ROI = 60

print(marlin.ROI)  # 60
print(viraj.ROI)   # 8
print(Bank.ROI)    # 8