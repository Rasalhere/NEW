# Program to demonstrate the dir() function

# Function to list the attributes and methods of an object
def list_attributes(obj):
    return dir(obj)

# Input from the user
user_input = input("Enter a value (e.g., a number, string, list): ")

# Convert input to a string, number, or list for demonstration
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

# Get the attributes and methods and display them
attributes = list_attributes(value)
print(f"The attributes and methods of the object are:\n{attributes}")
