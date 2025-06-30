# WRITE YOUR CODE HERE

# Dictionaries Exercise 4

def is_nested(input_dict):
  """
  Takes a dictionary and returns True if any of its values are a list,
  tuple, or dictionary; otherwise, returns False.

  Args:
    input_dict: The dictionary to check.
  
  Returns:
    A boolean value: True if nested, False otherwise.
  """
  # We can iterate directly through the values of the dictionary.
  for value in input_dict.values():
    # The isinstance() function is perfect for checking if a variable
    # is of a particular type. We can pass a tuple of types to check
    # against multiple possibilities at once.
    if isinstance(value, (list, tuple, dict)):
      # If we find even one value that is a list, tuple, or dict,
      # we know the dictionary is nested, and we can return True immediately.
      return True
      
  # If the loop completes without finding any nested structures,
  # we can safely return False. This line is only reached if the
  # 'return True' inside the loop is never triggered.
  return False


# test code below
if __name__ == "__main__":

  # --- Test Case 1 ---
  print("--- Test Case 1 ---")
  # Expected output: False
  example_dict_1 = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }
  print(is_nested(example_dict_1))

  # --- Test Case 2 ---
  print("\n--- Test Case 2 ---")
  # Expected output: True
  example_dict_2 = {
    1 : (2, 3), # This is a tuple
    4 : 'four',
    5 : 'five'
  }
  print(is_nested(example_dict_2))

  # --- Test Case 3 ---
  print("\n--- Test Case 3 ---")
  # Expected output: True
  example_dict_3 = {
    1 : 'one',
    2 : {3 : 4}, # This is a dictionary
    5 : 'five'
  }
  print(is_nested(example_dict_3))

  # --- Test Case 4 ---
  print("\n--- Test Case 4 ---")
  # Expected output: True
  example_dict_4 = {
    1 : 'one',
    2 : 'two',
    3 : [4, 5] # This is a list
  }
  print(is_nested(example_dict_4))
