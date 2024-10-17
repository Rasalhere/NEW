# Program to find the maximum of three numbers

# Function to find the maximum
def find_max(x, y, z):
    return max(x, y, z)

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate and display the maximum value
result = find_max(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is {result}.")
