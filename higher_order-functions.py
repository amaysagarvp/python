# lamda functions
# sum=lambda x,y,z : x+y+z
# mul=lambda x,y : x*y
# squre=lambda x:x**2

# print(sum(5,10,15))
# print(mul(10,7))
# print(squre(7))

#HIGHER ORDER FUNCTIONS
# def greet(name):
#     return f"Hello,{name}"
# def morning(name):
#     return f"good morning,{name}"
# def welcome_message(func,user_name):
#     message= func(user_name)
#     print(message)
# welcome_message(greet,"amay")
# welcome_message(morning,"amay")

#real life example
# def chef(recipe):
#     print("cooking in progress")
#     dish=recipe()
#     print("dish is ready")
#     return dish
# def make_pasta():
#     return "pasta"
# def make_pizz():
#     return "pizza"

# print(chef(make_pasta))

# return another function

# def make_multiplier(n):
#     def multiplier(x):
#         return x*n
#     return multiplier
# test = make_multiplier(4)
# print(test(5))
# print(test(10))

#
# def create_discount(percent):
#     def discount(price):
#         return price- (price*percent/100)
#     return discount
# student_discount =create_discount(15)
# normal_discount =create_discount(5)
# employe_discount=create_discount(20)
# print("student discount:",student_discount(500))
# print("normal discount:",normal_discount(1500))
# print("employe discount:",employe_discount(700))

#map example