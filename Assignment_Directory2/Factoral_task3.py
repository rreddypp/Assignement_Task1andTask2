def factorial(a):
    if a == 0 or a == 1:  # Base case
        return 1
    else:
        return a * factorial(a - 1)  # Recursive call

# Taking input from the user
a = int(input("Enter the number: "))

# Calling the function
res = factorial(a)

# Printing the result
print("Factorial of", a, "is:", res)
print("Thank you!")