from typing import List
import math

def fuel_used(list: List[int], target: int) -> int:
  return sum([abs(x - target) for x in list])

def abs_geometric_diff(x: int, y: int) -> int:
  diff = abs(x - y)
  return diff * (diff + 1) // 2

def fuel_used_increasing(list: List[int], target: int) -> int:
  return sum([abs_geometric_diff(x, target) for x in list])

def naive(list: List[int]) -> int:
  min_target = 0
  min_score = fuel_used(list, min_target)
  for i in range(min(list), max(list)+1):
    new_score = fuel_used(list, i)
    if new_score < min_score:
      min_score = new_score
      min_target = i
  return min_target

def naive_geometric(list) -> int:
  min_target = 0
  min_score = fuel_used_increasing(list, min_target)
  for i in range(min(list), max(list)+1):
    new_score = fuel_used_increasing(list, i)
    if new_score < min_score:
      min_score = new_score
      min_target = i
  return min_target

def get_input() -> List[int]:
  with open('input.txt') as f:
    return [int(x) for x in f.read().strip(' \n').split(',')]

def score(list: List[int], target):
  print(f"{target}: {fuel_used(list, target)}")

def score_geometric(list, target):
  print(f"{target}: {fuel_used_increasing(list, target)}")

def p1():
  positions = get_input()
  x = naive(positions)
  score(positions, x)

def p2():
  positions = get_input()
  x = naive_geometric(positions)
  score_geometric(positions, x)

p1()
p2()
print(abs_geometric_diff(16, 5))