# try:
#     num=int(input("enter a number"))
#     print(10 / num)
# except:
#     print("oops ! somthing went wrong")

#
# try:
#     num=int(input("enter a number:"))
#     print(10 / num)
# except ZeroDivisionError:
#     print("You can't devide by zero")
# except ValueError:
#     print("Please enter a valid number")


#
try:
    num=int(input("enter a number:"))
    result = 10/num
except ZeroDivisionError:
    print("division by zero not allow")
except ValueError:
    print("enter only numbers.")
else:
    print("success! result is",result)
finally:
    print("program finished")
