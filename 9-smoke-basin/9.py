from os import read
from typing import Dict, List, Tuple
import math

def read_input() -> List[List[int]]:
  with open('input.txt') as f:
    return [[int(y) for y in x] for x in f.read().strip(' \n').split('\n')]

def get_low_points(array: List[List[int]]) -> Tuple[int, int]:
  output = []
  for i in range(len(array)):
    for j in range(len(array[i])):
      # check if lower than all the neighbors
      val = array[i][j]
      less = True
      if i-1 >= 0 and array[i-1][j] <= val:
        less = False
      elif i+1 < len(array) and array[i+1][j] <= val:
        less = False
      elif j-1 >= 0 and array[i][j-1] <= val:
        less = False
      elif j+1 < len(array[i]) and array[i][j+1] <= val:
        less = False
      if less:
        output.append((i, j))
  return output

def find_basin_size(map: List[List[int]], loc: Tuple[int, int], marking_map=None) -> int:
  if not marking_map:
    marking_map = [[False for x in y] for y in map]
  i, j = loc
  if not (i >= 0 and j >= 0 and i < len(map) and j < len(map[i])) or marking_map[i][j] or map[i][j] == 9:
    return 0
  sum = 1
  marking_map[i][j] = True
  sum += find_basin_size(map, (i-1, j), marking_map)
  sum += find_basin_size(map, (i+1, j), marking_map)
  sum += find_basin_size(map, (i, j-1), marking_map)
  sum += find_basin_size(map, (i, j+1), marking_map)
  return sum

def p1():
  arr = read_input()
  low_points = get_low_points(arr)
  risk_levels = [arr[i][j]+1 for i,j in low_points]
  print('sum of risk levels:', sum(risk_levels))

def p2():
  arr = read_input()
  low_points = get_low_points(arr)
  basin_sizes = [find_basin_size(arr, x) for x in low_points]
  sorted_sizes = sorted(basin_sizes)
  print('product of top three basin sizes:', math.prod(sorted_sizes[-3:]))

p1()
p2()