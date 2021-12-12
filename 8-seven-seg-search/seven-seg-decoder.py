from typing import Dict, List, Tuple

def get_input() -> List[Tuple[List[str], List[str]]]:
  output = []
  with open('input.txt') as f:
    lines = f.read().strip(' \n').split('\n')
    for line in lines:
      a,b = line.split(' | ')
      output.append((a.split(' '), b.split(' ')))
  return output

def is_1478(x: str):
  return len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7

# count the number of times 1478 occurs in the provided list of strings
def count_1478(input: List[str]):
  return len([x for x in input if is_1478(x)])

# test display, which assumes the wires are mapped normally to a 7-seg display
def display_seg(input: str, schema='abcdefg') -> str:
  a = schema[0] in input
  b = schema[1] in input
  c = schema[2] in input
  d = schema[3] in input
  e = schema[4] in input
  f = schema[5] in input
  g = schema[6] in input
  filters = []
  filters.append('02356789' if a else '14')
  filters.append('045689' if b else '1237')
  filters.append('01234789' if c else '56')
  filters.append('2345689' if d else '017')
  filters.append('0268' if e else '134579')
  filters.append('013456789' if f else '2')
  filters.append('0235689' if g else '147')

  # there should be only one digit that is contained in all the filters.
  candidates = [str(x) for x in range(10)]
  for filter in filters:
    candidates = [x for x in candidates if x in filter]
  if len(candidates) != 1:
    # print('no match', input, schema)
    return ''
  else:
    # print('match', input, schema, candidates[0])
    return candidates[0]


def generate_schemas(dicts: Dict[str, List[str]]) -> List[str]:
  output = []
  for a in dicts['a']:
    for b in dicts['b']:
      if b not in [a]:
        for c in dicts['c']:
          if c not in [a, b]:
            for d in dicts['d']:
              if d not in [a, b, c]:
                for e in dicts['e']:
                  if e not in [a, b, c, d]:
                    for f in dicts['f']:
                      if f not in [a, b, c, d, e]:
                        for g in dicts['g']:
                          if g not in [a, b, c, d, e, f]:
                            output.append(''.join([a, b, c, d, e, f, g]))
  return output        
              
# get the schema given the 10 possible digits that can be displayed
# returns dictionary mapping input wire to correct output wire
def get_schema(sentence: List[str]) -> str:
  # each string has several mappings that it could belong to.
  # try to eliminate using a clue strategy based on length of words
  filters = {i: 'abcdefg' for i in 'abcdefg'}

  for word in sentence:
    length = len(word)
    # 1
    if length == 2:
      filters['c'] = word
      filters['f'] = word
    # 7
    elif length == 3:
      filters['a'] = word
    # 4
    elif length == 4:
      filters['b'] = word
      filters['d'] = word

  print(filters)
  schemas = generate_schemas(filters)
  print(schemas)
  for schema in schemas:
    if all([display_seg(x, schema) for x in sentence]):
      return schema


# decode the line given a tuple containing schema for each digit and an output string to decode
def decode_line(line: Tuple[List[str], List[str]]) -> str:
  schema = get_schema(line[0])
  output = ''
  for word in line[1]:
    output += display_seg(word, schema)
  print(output)
  return output
  
def p1():
  outlist = [count_1478(x[1]) for x in get_input()]
  print(sum(outlist))

def p2():
  lines = get_input()
  sum_lines = sum([int(decode_line(x)) for x in lines])
  print(sum_lines)
  
# p1()
p2()
