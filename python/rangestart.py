# Program to demonstrate the range() function with start, stop, and step

# Function to generate a range of numbers
def generate_range(start, stop, step):
    return list(range(start, stop, step))

# Input from the user
start = int(input("Enter the starting value (start): "))
stop = int(input("Enter the stopping value (stop): "))
step = int(input("Enter the step value (step): "))

# Generate and display the range
result = generate_range(start, stop, step)
print(f"The generated range from {start} to {stop} with a step of {step} is: {result}")
