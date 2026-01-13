# num = int(input("enter a number"))
# if num>5:
#     print("grater")
# elif num==5:
#     print("equal")
# else:
#     print("smaller")


#real world
# mark = int(input("enter your mark"))
# if mark>90:
#     print("Grade A")
# elif mark>=75:
#     print("Grade B")
# elif mark>=50:
#     print("Grade C")
# else:
#     print("fail")

#Nested if
# age = 25
# citizen = True

# if age>=18:
#     if citizen:
#         print("You can vote")
#     else:
#         print("you must be a citizen to vote")
# else:
#     print("your are very young to vote") #2 input

#check even or odd
# even =int(input("enter you number"))
# if even % 2==0:
#     print("this is even number")
# else:
#     print("this is odd number")

#1
# purchase = int(input("enter your purchase amount"))
# if purchase>=1000:
#     print(" you got 10% discount")
# else:
#     print("no discount")

#2
# person = int(input("enter your age"))
# if person<=13:
#     print("child")
# elif person<=19:
#     print("teenager")
# else:
#     print("adult")

#3 password check
# password = "python123"
# if password=="python123":
#     print("Access Granted")
# else:
#     print("Access Denied")

#4 electricity bill
# unit = int(input("enter unit"))
# if unit <100:
#     amount = unit * 5
# elif unit <=200:
#     amount = (100 * 5)+(unit - 100)*7
# else:
#     amount =(100*5)+(100*7)+(unit-200)*10  #try
# print("total amount ",amount)

#7 discount
# coustmer = int(input("enter you amount"))
# if coustmer>5000:
#     print("20% off")
# elif coustmer>2000:
#     print("10% off")
# else:
#     print("no off")

#8
# a = int(input("enter first"))
# b = int(input("enter secon"))
# c = int(input("enter third"))
# if a== b ==c:
#     print(" Equilateral ")
# elif a==b or b == c or a==c:
#     print("isosceles triangle")

#9

# a = (input("enter a charcter:"))
# if a.isupper():
#     print("Upper case letter")
# elif a.islower():
#     print("lowecase letter")
# elif a.isdigit():
#     print("Digit")
# else:
#     print("symbol")

#10 admin accsess
# atm =int(input("enter pin:"))
# if atm==1234:
#     print("Transition allowed")
# else:
#     print("invalid pin")

#11 atm 
correct_pin = 1234
pin = int(input("enter you pin"))
balance = float(input("enter your balance:"))
withdraw = float("input witthdraw monye:" )
if pin==correct_pin:
    if withdraw <= balance:
        balance = balance-withdraw
        print("withdraw success")
        print("remining balanc",balance)
    else:
        print("insufficient balance")
else:
    print("invalid pin")