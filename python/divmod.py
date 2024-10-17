# Program to demonstrate the divmod() function

# Function to perform division and modulus
def perform_divmod(x, y):
    return divmod(x, y)

# Input from the user
num1 = float(input("Enter the dividend (x): "))
num2 = float(input("Enter the divisor (y): "))

# Check for division by zero
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    # Calculate and display the quotient and remainder
    quotient, remainder = perform_divmod(num1, num2)
    print(f"The quotient and remainder of {num1} divided by {num2} are: {quotient} and {remainder}.")
