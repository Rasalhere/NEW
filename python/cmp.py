# Program to compare two numbers similar to cmp(x, y)

# Function to compare two numbers
def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

# Input from the user
num1 = float(input("Enter the first number (x): "))
num2 = float(input("Enter the second number (y): "))

# Compare the two numbers
result = compare(num1, num2)

# Display the result
if result == -1:
    print(f"{num1} is less than {num2}.")
elif result == 1:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")
