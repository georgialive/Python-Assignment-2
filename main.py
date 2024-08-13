import math

# Prompt the user for input and convert to floats
strA = input("Enter the value of 'a': ")
strB = input("Enter the value of 'b': ")
strC = input("Enter the value of 'c': ")
strD = input("Enter the value of 'd': ")

a = float(strA)
b = float(strB)
c = float(strC)
d = float(strD)

# Perform the calculations
num1 = a + b
num2 = num1 / c
num3 = num2 ** d
num4 = math.sqrt(num3)
answer = round(num4, 3)

# Output the result
print(f"The square root, rounded to 3 decimal places of a + b divided by c 
      raised to the power of d equals: {answer}")
