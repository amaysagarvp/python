num1 = float(input("enter your 1st number"))
num2 = float(input("enter your 2nd number"))

sum_result = num1 + num2

#differenc
difference = num1 - num2

#calculate product
product = num1 * num2

#calculate quotient
if num2 != 0:
    quotient = num1 / num2
    remainder = num1 % num2
else:
    quotient = "Undefined (division by zero)"
    remainder = "Undefined (division by zero)"

#calculate power
power = num1 ** num2

print(f"Sum:{sum_result}")

print(f"Difference:{difference}")

print(f"Product:{product}")

print(f"Quotient: {quotient}")

print(f"Power: {power}")
