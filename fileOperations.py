# file=open("example.txt","w")
# file.write("Hello this is from python...")
# file.close() #right

# read
# file=open("example.txt","r")
# # content=file.read()
# # content=file.readline()
# content=file.readlines()  #showning list
# print(content)
# file.close()

#Append mood
# file=open("example.txt","a")
# file.write("\nThis line was added latter")
# file.close()

#with open method
# with open("example.txt","r") as file:
#     content=file.read()
#     print(content)
# # No need to call file.close() manully 

# Read line by line
# with open("example.txt","r") as file:
#     for line in file:
#         print(line.strip())
# # this is efficient for large file

# Delete method
# import os
#check if file exists
# print(os.path.exists("example.txt"))
# Rename
# os.rename("example.txt","newfile001.txt")
# Delete
# os.remove("newfile001.txt")

#try
# try:
#     with open("nofile.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("The file was not found!")