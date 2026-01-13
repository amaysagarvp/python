#adding method
# fruits=["apple","banana"]
# fruits.append("cherry")
# print("append :",fruits)

# fruits.insert(2,"mango")
# print("insert :",fruits)

# fruits.extend(["grap","orange"])
# print("extend :",fruits)

#Remove
# fruits= ['apple', 'banana', 'mango', 'cherry', 'grap', 'orange']
# fruits.remove("apple")
# print("remove",fruits)

# #pop it remove the last element (default)
# fruits.pop()
# print("pop index 0:",fruits)

# #clear() remove all items
# fruits.clear()
# print("clear :",fruits)

#Searching & Counting
# fruits = ["apple", "banana", "cherry", "apple"]
# # index(value) → returns index of first occurrence
# print("index of 'banana':", fruits.index("banana"))
# # count(value) → counts occurrences
# print("count of 'apple':", fruits.count("apple"))

#Sorting & Reversing
# nums = [3, 1, 4, 2]
# # sort() → ascending order
# nums.sort()
# print("sorted ascending:", nums)
# # sort(reverse=True) → descending order
# nums.sort(reverse=True)
# print("sorted descending:", nums)
# # reverse() → reverse the list
# nums.reverse()
# print("reverse:", nums)

# Copying
# import   copy #built in module
# fruits = ["apple",["banana", "cherry"]]
# # copy() → shallow copy
# new_list = fruits.copy()
# # new_list = copy.deepcopy(fruits)
# fruits[1][0]="mango"
# print("fryits:", fruits)
# print("copy:", new_list)


#  Other Useful Functions
# nums = [1, 2, 3]
# # len() → number of items
# print("length:", len(nums))
# # max() → maximum value
# print("max:", max(nums))
# # min() → minimum value
# print("min:", min(nums))
# # sum() → sum of elements
# print("sum:", sum(nums))
# # sorted(list) → returns new sorted list
# print("sorted function:", sorted(nums, reverse=True))
# slist=sorted(nums,reverse=True)
# print(slist)
# print(nums)
# nums.sort(reverse=True)
# print(nums)

