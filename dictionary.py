student = {"name":"luffy","age":20,"grade":"king"}

print(student["name"]) #luffy
student["age"] #update
student["course"] = "cs" #add new
print(student)

student2 = {
    "name":"ace",
    "age":20,
    "course":"cs"
}

print(student2["name"]) #ace
print(student2.get("age")) #20
print(student2.keys()) #dict_keys(["name","age","course"])
print(student2.values()) #dict_values(["ace",20,"cs"])