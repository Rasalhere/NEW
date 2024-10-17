# Program to demonstrate the range() function with a single argument

# Function to generate a range of numbers
def generate_range(n):
    return list(range(n))

# Input from the user
n = 10  # Fixed value for range(10)

# Generate and display the range
result = generate_range(n)
print(f"The generated range from 0 to {n-1} is: {result}")
