# WRITE YOUR CODE HERE
# Dictionaries Exercise 1

def find_key(input_dict, value):
  """
  Takes a dictionary and a value, and returns the key associated with that value.

  Args:
    input_dict: The dictionary to search through.
    value: The value to find the corresponding key for.
  
  Returns:
    The key that maps to the given value. Returns None if the value is not found.
  """
  # Iterate through each key-value pair in the dictionary's items.
  # The .items() method is perfect for getting both the key and value together.
  for key, val in input_dict.items():
    # Check if the current item's value matches the value we're looking for.
    if val == value:
      # If it matches, we've found our key, so we return it.
      return key
  
  # If the loop finishes without finding the value, it means the value wasn't
  # in the dictionary. We can return None to indicate this.
  return None

# test code below
if __name__ == "__main__":
  # This dictionary is used for all three test cases.
  example_dict = {
    1 : ['red', 'blue', 'green'],
    'Josh Jung' : (9, 10),
    3 : {0 : 0},
    9000 : 'impale mat a'
  }

  print("--- Test Case 1 ---")
  # Expected output: Josh Jung
  key1 = find_key(example_dict, (9, 10))
  print(key1)

  print("\n--- Test Case 2 ---")
  # Expected output: 3
  key2 = find_key(example_dict, {0 : 0})
  print(key2)

  print("\n--- Test Case 3 ---")
  # Expected output: 9000
  key3 = find_key(example_dict, 'impale mat a')
  print(key3)
