list1 = ["apple",7,9,11,"kiwi",True,10,11,9]
list2 = [12,23,"orange"]

list3 = []  #emptylist
list4 = list()  #empty list using list()
list5 = list((1,2,3)) #Convert tuple to list

print("list:",list5)

print("list[0]:",list1[0]) #First element
print("list[-1]:",list1[-1]) #last element

print("list[:4]:",list1[:4]) # first 4 element
print("list[2:]:",list1[2:]) # from index 2 till end
print("list[2:5]:",list1[2:5]) # from index 2 to 4
print("list[::-1]:",list1[::-1]) # revers list

#concatenate
print("list + list1 :",list1 + list2)

#ressining element
list1[1] = "watermelon"
print("after ressinging :",list1)