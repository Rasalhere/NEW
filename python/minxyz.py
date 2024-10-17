# Program to find the minimum of three numbers

# Function to find the minimum
def find_min(x, y, z):
    return min(x, y, z)

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate and display the minimum value
result = find_min(num1, num2, num3)
print(f"The minimum of {num1}, {num2}, and {num3} is {result}.")
