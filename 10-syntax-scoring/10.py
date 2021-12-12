from typing import get_type_hints


def get_input():
  with open('input.txt') as f:
    return [x.strip(' \n') for x in f.readlines()]

def get_corruption_score(line: str) -> int:
  stack = []
  charmap = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
  }
  scoremap = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
  }
  for char in line:
    if char in charmap:
      stack.append(char)
    elif len(stack) and charmap[stack.pop()] == char:
      continue
    else:
      return scoremap[char]
  return 0

def get_completion_score(line: str) -> int:
  stack = []
  charmap = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
  }
  scoremap = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
  }
  score = 0
  for char in line:
    if char in charmap:
      stack.append(char)
    elif len(stack) and charmap[stack.pop()] == char:
      continue
    else:
      return 0
  # now, complete the rest of the line
  while len(stack):
    score *= 5
    score += scoremap[charmap[stack.pop()]]
  return score

def p1():
  lines = get_input()
  print('corruption score', sum([get_corruption_score(x) for x in lines]))

def p2():
  lines = get_input()
  scores  = sorted([x for x in [get_completion_score(x) for x in lines] if x])
  # take the median
  print('completion score', scores[len(scores)//2])

p1()
p2()