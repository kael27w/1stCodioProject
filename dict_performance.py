# testing dictionary performance

import timeit
import sys

large_num = int(sys.argv[1])
large_list = [i for i in range(large_num)]
large_dict = dict(zip(large_list, large_list))

def test_dict():
  for i in large_list:
    i in large_dict

dict_time = timeit.timeit(test_dict)

print(f'Dictionary time: {dict_time}')