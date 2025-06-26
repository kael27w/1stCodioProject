# WRITE YOUR CODE HERE

# Dictionaries Exercise 2

def move_to_bottom(input_dict, key_to_move):
  """
  Takes a dictionary and a key, and moves the specified key-value pair
  to the end of the dictionary. If the key does not exist, it returns an
  error string.

  Args:
    input_dict: The dictionary to modify.
    key_to_move: The key of the item to move.
  
  Returns:
    The modified dictionary, or an error string if the key is not found.
  """
  # First, check if the key exists in the dictionary.
  # This is the most efficient way to check for key existence.
  if key_to_move in input_dict:
    # Use the pop() method. It does two things:
    # 1. It removes the key-value pair.
    # 2. It returns the value associated with that key.
    value = input_dict.pop(key_to_move)
    
    # Now, re-assign the key with its value. In Python, adding a new item
    # to a dictionary places it at the end.
    input_dict[key_to_move] = value
    
    # Return the dictionary that has been modified in place.
    return input_dict
  else:
    # If the key was not found in the initial check,
    # return the specific error string.
    return "The key is not in the dictionary"


# test code below
if __name__ == "__main__":
  
  # --- Test Case 1 ---
  print("--- Test Case 1 ---")
  # Expected output: {2: 'two', 3: 'three', 1: 'one'}
  example_dict_1 = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }
  move_to_bottom(example_dict_1, 1)
  print(example_dict_1)

  # --- Test Case 2 ---
  print("\n--- Test Case 2 ---")
  # Expected output: {1: 'one', 3: 'three', 2: 'two'}
  example_dict_2 = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }
  move_to_bottom(example_dict_2, 2)
  print(example_dict_2)

  # --- Test Case 3 ---
  print("\n--- Test Case 3 ---")
  # Expected output: The key is not in the dictionary
  example_dict_3 = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }
  # For this case, we print the RETURN VALUE of the function
  result = move_to_bottom(example_dict_3, 4)
  print(result)

