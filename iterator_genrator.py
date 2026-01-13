# numbers=[10,20,30]
# it=iter(numbers)
# print(next(it))
# print(next(it))
# print(next(it))

# class Count:
#     def __init__(self,limit):
#         self.limit = limit
#         self.current = 1

#     def __init__(self):
#         return self
    
#     def __next__(self):
#         if self.current <= self.limit:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration
# c = Count(5)



#Genrator

# def numbers():
#     yield 1
#     yield 2
#     yield 3
# for n in numbers():
#     print(n)

#
# def count(limit):
#     i = 1
#     while i <= limit:
#         yield i
#         i += 1
# for n in count(5):
#     print(n)

#
def even_numbers(limit):
    for i in range(0,limit + 1,2):
        yield i
for n in even_numbers(10):
    print(n)




