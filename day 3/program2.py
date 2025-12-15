
# Demo of string slicing
input_string = input("Enter a string: ")

# Basic slicing
print(f"First 3 characters: {input_string[:3]}")
print(f"Characters from index 2 to 5: {input_string[2:6]}")
print(f"Last 4 characters: {input_string[-4:]}")

# Slicing with a step
print(f"Every second character: {input_string[::2]}")
print(f"Reversed string: {input_string[::-1]}")