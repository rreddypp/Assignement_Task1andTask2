import math  # Import the math module

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculate and display results
print("Square root of", num, "is:", math.sqrt(num))
print("Natural logarithm (log base e) of", num, "is:", math.log(num) if num > 0 else "Undefined (log of non-positive number)")
print("Sine of", num, "radians is:", math.sin(num))
print("Thank you!")
