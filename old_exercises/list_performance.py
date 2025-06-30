# testing list performance

import timeit
import sys

large_num = int(sys.argv[1])
large_list = [i for i in range(large_num)]

def test_list():
  for i in large_list:
    i in large_list

list_time = timeit.timeit(test_list)

print(f'List time: {list_time}')