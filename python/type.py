# Program to demonstrate the type() function

# Function to determine the type of a value
def determine_type(value):
    return type(value)

# Input from the user
user_input = input("Enter something: ")

# Determine the type of the input
# Convert to appropriate type for demonstration
try:
    # Try converting to integer
    value = int(user_input)
except ValueError:
    try:
        # If it fails, try converting to float
        value = float(user_input)
    except ValueError:
        # If it fails again, keep it as a string
        value = user_input

# Get the type and display it
result = determine_type(value)
print(f"The type of the input is: {result}")
