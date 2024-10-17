# Program to demonstrate the len() function

# Function to determine the length of an object
def get_length(obj):
    return len(obj)

# Input from the user
user_input = input("Enter a string or a list of items (comma-separated): ")

# Process the input
# Check if the input is a list or a string
if ',' in user_input:
    # Split the input into a list if it contains commas
    value = user_input.split(',')
    # Strip whitespace from each item
    value = [item.strip() for item in value]
else:
    # Otherwise, treat it as a string
    value = user_input

# Get the length and display it
length = get_length(value)
print(f"The length of the input is: {length}")
