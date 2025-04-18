import math

# Ask the user to enter a number
try:
    number = float(input("Please enter a positive number: "))

    if number <= 0:
        print("Please enter a number greater than zero for accurate calculations.")
    else:
        # Calculate using math module
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)  # Input is treated in radians

        # Display the results
        print(f"\nResults for number {number}:")
        print(f"✅ Square root: {square_root}")
        print(f"✅ Natural Logarithm (log base e): {natural_log}")
        print(f"✅ Sine (in radians): {sine_value}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
