
def read():
  with open('input.txt') as f:
    return f.read().strip(' \n').split('\n')

def p1(lines):
  num_cols = len(lines[0])
  gamma = ""
  epsilon = ""
  for col in range(num_cols):
    ones_count = 0
    for line in lines:
      if line[col] == '1':
        ones_count += 1
    if ones_count > len(lines) - ones_count:
      gamma += '1'
      epsilon += '0'
    else:
      gamma += '0'
      epsilon += '1'
    # print(f"col {col}: {ones_count} 1s out of {len(lines)}")
  # print(gamma)
  # print(epsilon)
  power = int(gamma, 2) * int(epsilon, 2)
  print('power:', power)

def most_common_bit(lines, col):
  ones_count = 0
  for line in lines:
    if line[col] == '1':
      ones_count += 1
  if ones_count >= len(lines) - ones_count:
    return '1'
  else:
    return '0'

# filter to lines that match the given bit at the given column
def filter_lines(lines, col, criteria):
  return [line for line in lines if line[col] == criteria]

def find_oxygen_rating(lines, col=0):
  bit = most_common_bit(lines, col)
  filtered_lines = filter_lines(lines, col, bit)
  # print(len(filtered_lines))
  if len(filtered_lines) == 1:
    return filtered_lines[0]
  else:
    return find_oxygen_rating(filtered_lines, col+1)

def find_co2_rating(lines, col=0):
  # flip the bit
  bit = '1' if most_common_bit(lines, col) == '0' else '0'
  filtered_lines = filter_lines(lines, col, bit)
  # print(len(filtered_lines))
  if len(filtered_lines) == 1:
    return filtered_lines[0]
  else:
    return find_co2_rating(filtered_lines, col+1)


def p2(lines):
  oxygen_rating = find_oxygen_rating(lines)
  co2_rating = find_co2_rating(lines)
  # print(oxygen_rating)
  # print(co2_rating)
  # print(int(oxygen_rating, 2))
  # print(int(co2_rating, 2))
  life_rating = int(oxygen_rating, 2) * int(co2_rating, 2)
  print('life rating:', life_rating)

lines = read()
p1(lines)
p2(lines)