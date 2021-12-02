# check for increases in a 3-number sliding window

with open('input.txt') as file:
  contents = file.read()

# print(contents)
moves = [x for x in contents.split('\n') if x]

total_distance = 0
total_depth = 0
for move in moves:
  [direction, distance] = move.split(' ')
  distance = int(distance)
  if direction == "forward":
    total_distance += distance
  elif direction == "down":
    total_depth += distance
  elif direction == "up":
    total_depth -= distance
  else:
    print('parsing error: ', direction, distance)
print(f'distance: {total_distance}')
print(f'depth: {total_depth}')
print(f'product: {total_depth*total_distance}')
  