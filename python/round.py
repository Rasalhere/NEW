# Program to round a number to a specified number of decimal places

# Function to round a number
def round_number(x, n):
    return round(x, n)

# Input from the user
num = float(input("Enter the number (x) to round: "))
decimal_places = int(input("Enter the number of decimal places (n): "))

# Calculate and display the rounded result
result = round_number(num, decimal_places)
print(f"The number {num} rounded to {decimal_places} decimal places is: {result}")
