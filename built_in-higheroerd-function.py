#MAP
# def squre(x):
#     return x * x
# def double(x):
#     return x*2

# numbers=[1,2,3,4]
# result=list(map(squre,numbers))
# result2=list(map(double,numbers))

# result3=list(map(lambda n:n*n,numbers))
# result4=list(map(lambda n:n*2,numbers))

# print(result)
# print(result2)
# print(result3)
# print(result4)

#Filter
# def is_even(n):
#     return n%2==0
# def is_odd(n):
#     return n%2!=0
# def gt_5(n):
#     return n>5
# numbers =[1,2,3,4,5,6,7,8,9]
# result=list(filter(is_even,numbers))
# result_odd=list(filter(is_odd,numbers))
# result_gt5=list(filter(gt_5,numbers))

# result1=list(filter(lambda n:n%2==0,numbers))
# result_odd1=list(filter(lambda n:n%2!=0,numbers))
# result_gt51=list(filter(lambda n:n>5,numbers))

# print(result)
# print(result_odd)
# print(result_gt5)

# print(result1)
# print(result_odd1)
# print(result_gt51)

#Reduce
# from functools import reduce
# def add(a,b):
#     return a+b
# numbers=[1,2,3,4,5,6,7,8,]
# result=reduce(add,numbers)
# result1=reduce(lambda a,b:a+b,numbers)
# result_mul=reduce(lambda a,b:a*b,numbers)

# print(result)
# print(result1)
# print(result_mul)

#Sorted
# students =[("anu",20),("rahul",18),("amay",23)]

# sorted_students = sorted(students,key=lambda x: x[1])
# print(sorted_students)