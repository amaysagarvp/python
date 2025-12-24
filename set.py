set1 = {1,2,3,4,5}
set2 = {"apple","banana","cherry"}
set3 = set([1,2,3,4]) #duplicate removed
print("set:",set3)

#adding & Removing
set1.add(6)
print("after add:",set1)
set1.remove(3) # remove element error if not present
print("after remove:",set1)
set1.discard(10) # no error if element not present

#set operators
a = {1,2,3,4}
b = {3,4,5,6}
print("Union:",a | b) #{1,2,3,4,5,6}
print("Intersection:",a & b) #{3,4}
print("Difference:",a-b) #{1,2}
print("Symmetic Diff:",a ^ b) #{1,2,5,6}