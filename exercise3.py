# WRITE YOUR CODE HERE

# Dictionaries Exercise 3

def swap(input_dict):
  """
  Takes a dictionary and returns a new dictionary where the keys and values
  have been swapped. If any value in the original dictionary is unhashable
  (and thus cannot be a key), it returns an error string.

  Args:
    input_dict: The dictionary to swap.
  
  Returns:
    A new dictionary with keys and values swapped, or an error string.
  """
  # --- Step 1: Validate that all values are hashable ---
  # Dictionary keys must be immutable (hashable). This includes types like
  # strings, numbers, and tuples. Lists and dictionaries are mutable (unhashable).
  # We must check this before attempting the swap.
  for value in input_dict.values():
    # We can check if the value's type is one of the common unhashable types.
    if isinstance(value, (list, dict)):
      return "Cannot swap the keys and values for this dictionary"

  # --- Step 2: Perform the swap ---
  # If the first loop completed, it means all values are safe to be used as keys.
  
  # Create a new empty dictionary to store the swapped pairs.
  swapped_dict = {}
  
  # Iterate through the original dictionary's items.
  for key, value in input_dict.items():
    # For the new dictionary, use the original value as the key
    # and the original key as the value.
    swapped_dict[value] = key
    
  return swapped_dict


# test code below
if __name__ == "__main__":

  # --- Test Case 1 ---
  print("--- Test Case 1 ---")
  # Expected output: {'one': 1, 'two': 2, 'three': 3}
  example_dict_1 = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }
  swapped_1 = swap(example_dict_1)
  print(swapped_1)

  # --- Test Case 2 ---
  print("\n--- Test Case 2 ---")
  # Expected output: Cannot swap the keys and values for this dictionary
  example_dict_2 = {
    1 : [2, 3], # list is unhashable
    4 : 'four',
    5 : 'five'
  }
  swapped_2 = swap(example_dict_2)
  print(swapped_2)

  # --- Test Case 3 ---
  print("\n--- Test Case 3 ---")
  # Expected output: Cannot swap the keys and values for this dictionary
  example_dict_3 = {
    1 : 'one',
    2 : {3 : 4}, # dict is unhashable
    5 : 'five'
  }
  swapped_3 = swap(example_dict_3)
  print(swapped_3)

  # --- Test Case 4 ---
  print("\n--- Test Case 4 ---")
  # Expected output: {'one': 1, 'two': 2, (4, 5): 3}
  example_dict_4 = {
    1 : 'one',
    2 : 'two',
    3 : (4, 5) # tuple is hashable
  }
  swapped_4 = swap(example_dict_4)
  print(swapped_4)
