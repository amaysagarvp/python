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

#2 covert
# def convert_usd(amount_inr):
#     usd=amount_inr/83
#     return usd
# print(convert_usd(8300))

#3 discount
# def final_price(price,discount):
#     return price-(price*discount/100)
# print(final_price(1000,30))

#4 deliver charges
# def delivery_charge(distance):
#     if distance<5:
#         # print("30$")
#         return 30
#     elif distance<10:
#         # print("50rupees")
#         return 50
#     else:
#         return 100
# print(delivery_charge(15))

#default parameter
#1 seat booking
# def book_ticket(name,seat="genaral"):
#     print(f"ticket booked for{name}")
#     print(f"seat type:{seat}")
# book_ticket("amay","sleeper")

#2email
# def send_email(to,subject="NoSubject",message="empty"):
#     print("Sending Email....")
#     print("To",to)
#     print("subject",subject)
#     print("message",message)
# send_email("amaysagar60@gmail.com",subject="info",message="i will call you latter")

#keyword arguments
#1 creataccount
# def creat_account(name,age,balance):
#     print("Account Created Successfully")
#     print("Name",name)
#     print("Age",age)
#     print("balance",balance)
# creat_account(balance=2000000,age=25,name="amay")

#2
# def movie_ticket(movie,seat,price):
#     print("movie ticket booked")
#     print("movie",movie)
#     print("seat",seat)
#     print("price",price)
# movie_ticket(movie="kgf",seat="b12",price=180)

#variable length argument
#calculate
# def calculate_total(*price):
#     return sum(price)
# print(calculate_total(100,250,80))

#average
# def average_score(*score):
#     if len(score) ==0:
#         return 0
#     return sum(score) /len(score)
# print(average_score(80,90,75))

#name
# def combine_names(*names):
#     return " ".join(names)

# print(combine_names("Amay", "Sagar", "VP"))

#6 variable length keyword argument
# def student_profile(**details):
#     print("student profile")
#     for key,value in details.items():
#         print(f"{key}:{value}")
# student_profile(
#     name="amay",
#     age=23,
#     class_name="12th",
#     city="kozhikode",
#     grade="A",
# )

#fooditems
# def place_order(**items):
#     print("food bill")
#     total=0
#     for item,price in items.items():
#         print(f"{item}:${price}")
#         total += price

#     print("---------")
#     print(f"total amount:${total}")

# place_order(
#     burger=100,
#     pizza=90,
#     coke=50,
# )

#
# def employe_recorde(**info):
#     print("employe details")
#     for key,value in info.items():
#         print(f"{key}:{value}")
# employe_recorde(
#     id=7,
#     name="amaysgagar",
#     designation="fullstack developer",
#     salary=50000,
#     department="frontend",

# )

#advance
#atm withdraw
# def atm_withdraw(balance,amount=20000):
#     if amount<20000:
#         print("you can withdraw")
#     else:
#         print("you cant withdraw")
# atm_withdraw(20000,)
# print(atm_withdraw)
# def atm_withdraw(balance,amount,limit=20000):
#     if amount > limit:
#         return"withdraw exceed daily limit"
#     elif amount > balance:
#         return"insufficent balance"
#     else:
#         return balance-amount
# print(atm_withdraw(30000,5000))

