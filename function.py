#example of simple function
# def greet():
#     print("hello,welcome to python!")
# greet()

#parameter
# def greet(name):
#     print(f"hello,{name}")
# greet("amay")
# greet("sagar")

# function to add two numbers
# def add(num1,num2):
#     print(num1+num2)
#     return num1+num2
# add(2,5)
# add(40,10)
# x=10
# y=60
# add(x,y)
# print(add(x,y))

#function with return value
# def add(num1,num2):
#     return num1+num2
# x=add(3,5)
# print(f"x={x}")
# print(f"sum:{add(10,40)}")
# res=add(6,7)
# print("res:",res)
# print(add(2,6))

#function to print number 1 to n 
# def print_num(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum
# total=print_num(5)
# print(f"total :{total}")

#factorial of a number 
# def fact(n):
#     fct=1
#     for i in range(1,n+1):   #05/25
#         fct *= i
#     return fct
# result=fact(5)
# print(f"fact:{result}")

#febinoci
# def febi(n):
#     a,b=0,1
#     i=0
#     while i< n:
#         print(a,end="")
#         a,b = b,a+b
#         i+=1
# num=int(input("enter n:"))
# febi(num)

#Default parameter
# def greet(name="guest"):
#     print("hello",name)
# greet()
# greet("amay")

#keyword argument
# def student(name,age,is_student=True):
#     print("name:",name,"age:",age,"is_student",is_student)

# student(is_student=True,age=23,name="amay")
# student("raj",23)

#Variable number of arguments
# def total(*numbers):
#     sum=0
#     for n in numbers:
#         sum += n #dought on n
#     return sum
# print(total(2,3,4,5))
# print(total(1,2))
# print(total(7,9,11))

#variable length of argument
# def show_student(*students):
#     for i, student in enumerate(students, start=1):
#         print(f"\nStudent {i}:")
#         for key, value in student.items():
#             print(key, ":", value)

# show_student(
#     {"name": "amay", "age": 23, "grade": "A"},
#     {"name": "navi", "age": 23, "grade": "A"},
#     {"name": "gb", "age": 24, "grade": "A"}
# )

#variable #using ** kwargs(keywordarguments)
# def info(**details):
#     for k,v in details.items():
#         print(f"{k}:{v}")

# info(name="amay",age=20,city="kozhikode")
# info(name="sagar",age=21,city="kozhikode",email="amay@.com",phone=9999999999)

#
# def student_details(*args,**kwargs):
#     print("extra info:",args)  #tuple values
#     print("student details:")
#     for key,value in kwargs.items():
#         print(key,":",value)
# #call with both
# student_details("batch B1","python Fullstack",name="rahul",age=23,grade="B",city="Delhi")

#
# def generate_bill(**items):
#     print("customer bill")
#     print("----------")
#     total = 0
#     for item,price in items.items():
#         print(f"{item} : ${price}")
#         total += price
#     print("----------")
#     print(f"total Amount = ${total}")

# generate_bill(apple=50,milk=30,bread=40,rice=200)
# generate_bill(orange=70,book=30,bread=60,rice=70)

#welcome message 
# def greet_coustomer():
#     print("welcome to our shop")
# def greet_menu():
#     print("food menu")
#     print("1.pizza")
#     print("2.french fries")
#     print("3.kanji")
#     print("4.kappa")

# greet_coustomer()
# greet_menu()

