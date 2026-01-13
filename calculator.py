def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def devide(a,b):
    if b==0:
        return "cannot devide by zero"
    return a/b
    
if __name__== "__main__":
    print(devide(10,2))
