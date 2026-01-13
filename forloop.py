# for i in range(6): #0-5
#     print(i)

# for i in range(1,6): # 1-5
#     print(i)

# for i in range(1,10,2): # 1,3,5,7,9
#     print(i)

# for i in range(0,10,2):
#     print(i)

# sum of numbers 1 to 100
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

# sum=0
# n=int(input("enter number"))
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# total = 0
# for i in range(1,11):
#     total+=i
# print({total})

# list1=[10,20,30,40]
# for i in list1:
#     print(i)
# for index,value in enumerate(list1): #check
#     print(index,value)

# 
# str1="hello"
# for char in str1:
#     print(char)

#
# fruits=["apple","mango","burry"]
# for index,fruit in enumerate(fruits,start=1):
#     print(index,fruit)

#largest number in the list
# marks=[30,29,50,46,60]
# largest=marks[0]
# for mark in marks:
#     if mark > largest:
#         largest=mark
# print(f"largest:{largest}")

#01/01/26
#smallest
# marks=[30,29,50,46,60]
# largest=marks[0]
# smallest=mark[0]
# for mark in marks:
#     if mark > largest:
#         largest=mark
#     if mark < largest:
#         smallest=mark    
# print(f"largest:{largest}")
# print(f"smallest:{smallest}")

# #forloop in dictionary value & key 
# student = {"name":"rahul","age":20,"grade":"A"}
# for i in student:
#     print(i,student[i])

# student = {"name":"rahul","age":20,"grade":"A"}
# # for i in student.values():
# #     print(i)
# for key,value in student.items():
#     print(key,value)

#reverse
# word="Malayalam"
# reverse = ''
# for char in word:
#     reverse=char+reverse
# print(f"revers:{reverse}")

#
# word = input("enter a word:")
# reverse=""
# for char in word:
#     reverse=char+reverse
# print(f"revers:{reverse}")
# if word==reverse:
#     print(f"{word} is palindrom")
# else:
#     print(f"{word} is not a palindrom")

# star print
# for i in range(4):
#     for j in range(i+1):#(4)
#         print("* ",end="")
#     print()

#
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1, end="")
#     print()

#countin fruits
# fruits=["apple","banana","mango","apple","apple"]
# counte=0
# for fruits in fruits:
#     if fruits =="apple":
#         counte +=1
# print(counte)
# total=len(fruits) #total value 
# print(total)

#shopping cart total
prices=[120,230,345,290,90]
total=0
for price in prices:
    total += price
price(total)
