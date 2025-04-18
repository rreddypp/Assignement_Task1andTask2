# Define the factorial function
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Get input from the user and convert it to integer
sample_number = int(input("Please enter a number: "))
output = factorial(sample_number)

# Print the output
print(f"The factorial of {sample_number} is: {output}")

