def histogram(data):
  """
  Prints a histogram to the screen for a given list of integers.

  Args:
    data: A list of integers (e.g., [4, 9, 7]).
  """
  for num in data:
    # Print the number, a colon, and then the asterisk repeated 'num' times
    print(f"{num}: {'*' * num}")

# Example usage:
histogram([4, 9, 7])