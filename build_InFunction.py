# # Create a string variable and store some text in it
# s = "Python String and variable"
# # Converts all letters in the string to lowercase
# print("Lowercase:", s.lower())       
# # Converts all letters in the string to uppercase
# print("Uppercase:", s.upper())        
# # Converts the first letter of each word to uppercase
# print("Title Case:", s.title())      
# # Converts only the first letter of the string to uppercase, rest to lowercase
# print("Capitalize:", s.capitalize()) 
# # Swaps the case of each letter (uppercase becomes lowercase and vice versa)
# print("Swapcase:", s.swapcase())     
# # Similar to lower(), but more powerful for case-insensitive comparisons (used for languages with special characters)
# print("Casefold:", s.casefold())

#stri and lstrip 
# # Create a string with extra spaces at the beginning and end
# s = "   Hello Python   "
# # Print the original string using repr() to clearly show spaces
# print("Original:", repr(s))          
# # Removes spaces from both the beginning and the end of the string
# print("strip():", repr(s.strip()))   
# # Removes spaces only from the left side (beginning) of the string
# print("lstrip():", repr(s.lstrip()))  
# # Removes spaces only from the right side (end) of the string
# print("rstrip():", repr(s.rstrip()))

#replace substring

#create a string variable with some text
# s="hello world hello world"
# #print the original string
# print("Original:",s)
# #Replace the word 'word' with 'python' using the replace() method
# print("Replace 'world' with 'python':",s.replace("world","python"))
# print(s)

#split/join

# s="apple,banana,cherry"
# print("Orginal:",s)
# #split the string into a list using comma(',') as the separator
# print("split by comma:",s.split(","))
# #create a list of word
# words=["python", "is", "fun"]
# #join the list element into a single string separated by a space
# print("join with space:"," ".join(words))

#lslash

# path="/Home/user/document/file.txt"
# Islash=path.rfind("/")
# filename=path[Islash+1:]  #dought
# print(filename)

# s="hello world"
# print("Find 'o':",s.find("o"))

# print("Rfind 'o':",s.rfind("o"))

# #find the position (index) of 'w' in the string
# print("Index 'w':",s.index("w"))

#count

# s="banana"
# print("count 'a':",s.count("a"))

#strats with ends with
# s="python"
# #check the string strats wit py
# print("starts with 'py':",s.startswith("pyt"))

# print("Ends with 'on':",s.endswith("on"))

#Type of character
# Create string variables
# s1 = "Hello"
# s2 = "123"
# s3 = "Hello123"
# s4 = "   "  # String containing only spaces
# # Check if all characters in s1 are alphabet letters
# print("s1.isalpha():", s1.isalpha())   
# # Check if all characters in s2 are digits
# print("s2.isdigit():", s2.isdigit())   
# # Check if all characters in s3 are alphanumeric (letters or numbers)
# print("s3.isalnum():", s3.isalnum())  
# # Check if s4 contains only whitespace
# print("s4.isspace():", s4.isspace())   
# # Check if s1 follows title case (first letter uppercase, rest lowercase)
# print("s1.istitle():", s1.istitle())   
# # Check if all letters in s1 are uppercase
# print("s1.isupper():", s1.isupper())  
# # Check if all letters in s1 are lowercase
# print("s1.islower():", s1.islower())

#
# s="42"
# s2="567"
# print("zfills(5):",s.zfill(5))
# print("zfills(5):",s2.zfill(5))

#center & left & right
# print("Center(6,''):",s.center(20,' '))

# print("Ljust(6,'_'):",s.ljust(20,'_'))

# print("Rjust(6,'_'):",s.rjust(20,'_'))


# Sample data: student ID, name, and marks
students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 23, "name": "Bob", "marks": 92},
    {"id": 7, "name": "Charlie", "marks": 78},
    {"id": 15, "name": "Diana", "marks": 100}
]
def get_marks(student):
    return student['marks']
# Sort students by marks (descending)   
students_sorted=sorted(students,reverse=True,key=get_marks)
title="Student Report Card"
print("\n"+ title.center(40,"="))
print("ID".center(6),"Name".ljust(15),"Marks".rjust(5))
print("-"*40)
for student in students_sorted:
    student_id = str(student['id']).zfill(3)
    name=student['name'].ljust(15)
    marks=str(student['marks']).rjust(5)
    print(student_id.center(6),name,marks)
print("="*40)


#partition
s="hello-world-python"
print("partition by '-':",s.partition("-"))

print("Rpartition by '-':",s.rpartition("-"))