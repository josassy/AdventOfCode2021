from typing import List, Tuple

class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
  
  def __repr__(self) -> str:
      return f"({self.x},{self.y})"
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)


class Board:
  def __init__(self) -> None:
    self.board = {}
    self.overlap_count = 0

  def __repr__(self) -> str:
    return str(self.board)

  def insert_point(self, p: Point):
    if p.x not in self.board:
      self.board[p.x] = {}
    row = self.board[p.x]
    if p.y not in row:
      row[p.y] = 1
    else:
      row[p.y] = row[p.y] + 1
      if row[p.y] == 2:
        self.overlap_count += 1
  
  def insert_line(self, p1: Point, p2: Point):
    if p1.x == p2.x:
      start, end = (p1.y, p2.y) if p1.y < p2.y else (p2.y, p1.y)
      for i in range(start, end + 1):
        self.insert_point(Point(p1.x, i))
    elif p1.y == p2.y:
      start, end = (p1.x, p2.x) if p1.x < p2.x else (p2.x, p1.x)
      for i in range(start, end + 1):
        self.insert_point(Point(i, p1.y))
    elif abs(p1.x - p2.x) == abs(p1.y - p2.y):
      dx = 1 if p1.x < p2.x else -1
      dy = 1 if p1.y < p2.y else -1
      d = Point(dx, dy)
      currentPoint = p1
      for i in range(abs(p1.x - p2.x)+1):
        self.insert_point(currentPoint)
        currentPoint += d

    else:
      print('error: invalid line', p1, p2)

def read_input(input: str) -> List[Tuple[Point, Point]]:
  output = []
  for line in input.strip(' \n').split('\n'):
    p1, p2 = [Point(int(x[0]), int(x[1])) for x in [x.split(',') for x in line.split(' -> ')]]
    output.append((p1, p2))
  return output

def read_file() -> str:
  with open('input.txt') as f:
    return f.read()

def part1():
  lines = read_input(read_file())
  # use a nested map to place points as they are generated
  board = Board()
  for p1, p2 in lines:
    board.insert_line(p1, p2)
  print(board.overlap_count)    

part1()